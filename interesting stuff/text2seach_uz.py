from __future__ import annotations

import argparse
import asyncio
import glob
import os
import re
import sys
from pathlib import Path
from typing import Iterable

# ru-RU-SvetlanaNeural   Female
# ru-RU-DariyaNeural     Female
# ru-RU-DmitryNeural     Male

# en-US-JennyNeural    Female
# en-US-AriaNeural     Female
# en-US-AvaNeural      Female
# en-US-EmmaNeural     Female
#
# en-US-GuyNeural      Male
# en-US-AndrewNeural   Male
# en-US-BrianNeural    Male
# en-US-DavisNeural    Male

try:
    import edge_tts
except ImportError:
    print(
        "Missing package: edge-tts\n"
        "Install it with:\n"
        "  python -m pip install edge-tts",
        file=sys.stderr,
    )
    raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert one or more TXT files to MP3.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=r"""
Examples:
  python text2speech.py text.txt
  python text2speech.py text.txt next.txt other.txt
  python text2speech.py "text.txt,next.txt,other.txt"
  python text2speech.py "C:\Users\User\Desktop\*.txt"
  python text2speech.py "C:\Users\User\Desktop"
  python text2speech.py text.txt -o result.mp3
  python text2speech.py text.txt next.txt --output-dir "C:\MP3"
  python text2speech.py text.txt --language en-US
  python text2speech.py text.txt --voice uz-UZ-MadinaNeural
  python text2speech.py --list-voices --language uz-UZ
  python text2speech.py --list-voices --language ru-female
By default, every MP3 is saved beside its source TXT file.
""",
    )

    parser.add_argument(
        "inputs",
        nargs="*",
        help="TXT files, comma-separated files, folders, or wildcard patterns.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Exact MP3 path. Only valid with one input file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Folder where all generated MP3 files will be saved.",
    )
    parser.add_argument(
        "--language",
        default="uz-UZ",
        help="Voice locale. Default: uz-UZ.",
    )
    parser.add_argument(
        "--voice",
        help="Exact voice name. When omitted, a voice is selected automatically.",
    )
    parser.add_argument(
        "--gender",
        choices=("Female", "Male"),
        default="Female",
        help="Preferred gender for automatic voice selection. Default: Female.",
    )
    parser.add_argument(
        "--rate",
        default="+0%",
        help='Speech rate, for example "-10%%" or "+15%%". Default: +0%%.',
    )
    parser.add_argument(
        "--volume",
        default="+0%",
        help='Volume, for example "-10%%" or "+20%%". Default: +0%%.',
    )
    parser.add_argument(
        "--pitch",
        default="+0Hz",
        help='Pitch, for example "-10Hz" or "+5Hz". Default: +0Hz.',
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Search folders recursively for TXT files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing MP3 file.",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="List voices, optionally filtered by --language, and exit.",
    )
    return parser.parse_args()


def split_input_arguments(values: Iterable[str]) -> list[str]:
    result: list[str] = []
    for value in values:
        for part in value.split(","):
            part = part.strip().strip('"').strip("'")
            if part:
                result.append(part)
    return result


def collect_txt_files(values: Iterable[str], recursive: bool) -> list[Path]:
    files: list[Path] = []

    for raw_value in split_input_arguments(values):
        expanded = os.path.expandvars(os.path.expanduser(raw_value))
        path = Path(expanded)

        if path.is_file():
            if path.suffix.lower() != ".txt":
                raise ValueError(f"Not a TXT file: {path}")
            files.append(path)
            continue

        if path.is_dir():
            pattern = "**/*.txt" if recursive else "*.txt"
            files.extend(item for item in path.glob(pattern) if item.is_file())
            continue

        matches = [
            Path(match)
            for match in glob.glob(expanded, recursive=recursive)
            if Path(match).is_file() and Path(match).suffix.lower() == ".txt"
        ]
        if matches:
            files.extend(matches)
            continue

        raise FileNotFoundError(f"File, folder, or pattern not found: {raw_value}")

    unique: list[Path] = []
    seen: set[str] = set()
    for path in files:
        resolved = path.resolve()
        key = os.path.normcase(str(resolved))
        if key not in seen:
            seen.add(key)
            unique.append(resolved)

    if not unique:
        raise FileNotFoundError("No TXT files found.")

    return unique


def read_text(path: Path) -> str:
    encodings = (
        "utf-8-sig",
        "utf-8",
        "utf-16",
        "utf-16-le",
        "utf-16-be",
        "cp1251",
        "cp1252",
    )

    for encoding in encodings:
        try:
            text = path.read_text(encoding=encoding)
            text = text.replace("\x00", "")
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r"\n{3,}", "\n\n", text)
            text = text.strip()
            if text:
                return text
        except (UnicodeDecodeError, UnicodeError):
            continue

    raise UnicodeError(f"Could not read text encoding: {path}")


def output_path_for(path: Path, args: argparse.Namespace, count: int) -> Path:
    if args.output:
        if count != 1:
            raise ValueError("-o/--output can only be used with one TXT file.")
        output = args.output.expanduser()
        if output.suffix.lower() != ".mp3":
            output = output.with_suffix(".mp3")
        output.parent.mkdir(parents=True, exist_ok=True)
        return output.resolve()

    output_dir = args.output_dir.expanduser() if args.output_dir else path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    return (output_dir / f"{path.stem}.mp3").resolve()


async def available_voices() -> list[dict]:
    return await edge_tts.list_voices()


async def choose_voice(language: str, requested: str | None, gender: str) -> str:
    voices = await available_voices()

    if requested:
        names = {voice["ShortName"] for voice in voices}
        if requested not in names:
            raise ValueError(
                f"Voice not found: {requested}\n"
                "Run with --list-voices to see available voices."
            )
        return requested

    locale_matches = [
        voice for voice in voices if voice.get("Locale", "").lower() == language.lower()
    ]
    if not locale_matches:
        raise ValueError(
            f"No voice found for language locale: {language}\n"
            "Run with --list-voices to see available locales."
        )

    preferred = [
        voice for voice in locale_matches if voice.get("Gender") == gender
    ]
    selected = preferred[0] if preferred else locale_matches[0]
    return selected["ShortName"]


async def list_voices(language: str) -> None:
    voices = await available_voices()
    filtered = [
        voice
        for voice in voices
        if not language or voice.get("Locale", "").lower() == language.lower()
    ]

    if not filtered:
        print(f"No voices found for: {language}")
        return

    for voice in filtered:
        print(
            f'{voice.get("ShortName", "")}  '
            f'[{voice.get("Gender", "")}, {voice.get("Locale", "")}]'
        )


async def convert_file(
    input_path: Path,
    output_path: Path,
    voice: str,
    rate: str,
    volume: str,
    pitch: str,
) -> None:
    text = read_text(input_path)
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        volume=volume,
        pitch=pitch,
    )
    await communicate.save(str(output_path))


def main() -> int:
    args = parse_args()

    try:
        if args.list_voices:
            asyncio.run(list_voices(args.language))
            return 0

        if not args.inputs:
            raise ValueError("Add at least one TXT file.")

        files = collect_txt_files(args.inputs, args.recursive)
        voice = asyncio.run(choose_voice(args.language, args.voice, args.gender))
        print(f"Voice: {voice}")

        created = 0
        skipped = 0

        for input_path in files:
            output_path = output_path_for(input_path, args, len(files))

            if output_path.exists() and not args.overwrite:
                print(f"Skip: {output_path} (use --overwrite to replace it)")
                skipped += 1
                continue

            print(f"Creating: {output_path}")
            asyncio.run(
                convert_file(
                    input_path,
                    output_path,
                    voice,
                    args.rate,
                    args.volume,
                    args.pitch,
                )
            )
            created += 1

        print(f"Finished. Created: {created}. Skipped: {skipped}.")
        return 0

    except KeyboardInterrupt:
        print("Cancelled.", file=sys.stderr)
        return 130
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())