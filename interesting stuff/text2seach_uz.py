from __future__ import annotations

import argparse
import ctypes
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import wave
from pathlib import Path

MODEL_URL = "https://models.silero.ai/models/tts/ru/v5_cis_base_nostress.pt"
MODEL_FILENAME = "v5_cis_base_nostress.pt"
SPEAKER = "uzb_saida"
SAMPLE_RATE = 48_000

EXPECTED_FILES = [
    "Tanqidiy_pedagogika_savol_javob.txt",
    "Ilmiy_tadqiqot_metodologiyasi_savol_javob.txt",
    "Pedagogik_diagnostika_va_korreksiya_savol_javob.txt",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Find three Uzbek question/answer TXT files on the Windows Desktop "
            "and create three Uzbek MP3 files there."
        )
    )
    parser.add_argument(
        "--desktop",
        type=Path,
        help="Optional Desktop folder path. Normally detected automatically.",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Generate only the first three question/answer blocks from every TXT file.",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=1.03,
        help="Playback speed without pitch change (0.5-2.0, default: 1.03).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing MP3 files without asking.",
    )
    return parser.parse_args()


def get_windows_desktop() -> Path:
    """Get the real Windows Desktop folder, including OneDrive redirection."""
    if os.name == "nt":
        buffer = ctypes.create_unicode_buffer(32768)
        # CSIDL_DESKTOPDIRECTORY = 0x0010
        result = ctypes.windll.shell32.SHGetFolderPathW(None, 0x0010, None, 0, buffer)
        if result == 0 and buffer.value:
            return Path(buffer.value)

    candidates = [
        Path.home() / "Desktop",
        Path.home() / "OneDrive" / "Desktop",
        Path.home() / "Рабочий стол",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return Path.home() / "Desktop"


def check_dependencies() -> None:
    missing: list[str] = []
    try:
        import torch  # noqa: F401
    except ImportError:
        missing.append("torch")

    try:
        import numpy  # noqa: F401
    except ImportError:
        missing.append("numpy")

    try:
        import imageio_ffmpeg  # noqa: F401
    except ImportError:
        missing.append("imageio-ffmpeg")

    if missing:
        packages = " ".join(missing)
        raise RuntimeError(
            "Missing packages: "
            + packages
            + "\n\nInstall them in PowerShell:\n"
            + "python -m pip install numpy imageio-ffmpeg\n"
            + "python -m pip install torch --index-url "
            + "https://download.pytorch.org/whl/cpu"
        )


def find_input_files(desktop: Path) -> list[Path]:
    files: list[Path] = []
    desktop_files = {p.name.lower(): p for p in desktop.glob("*.txt")}

    for filename in EXPECTED_FILES:
        exact = desktop / filename
        if exact.exists():
            files.append(exact)
            continue

        case_insensitive = desktop_files.get(filename.lower())
        if case_insensitive:
            files.append(case_insensitive)
            continue

        # Fallback: match the important words if the filename was slightly changed.
        words = [
            word
            for word in re.split(r"[_\s]+", Path(filename).stem.lower())
            if word not in {"savol", "javob"}
        ]
        matches = [
            path
            for path in desktop.glob("*.txt")
            if all(word in path.stem.lower() for word in words[:2])
        ]
        if len(matches) == 1:
            files.append(matches[0])
            continue

        raise FileNotFoundError(
            f"TXT file not found on Desktop:\n  {filename}\n\n"
            f"Expected Desktop folder:\n  {desktop}"
        )

    return files


def read_text_file(path: Path) -> str:
    encodings = ("utf-8-sig", "utf-8", "cp1251")
    for encoding in encodings:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeError(f"Cannot decode text file: {path}")


def clean_text(text: str) -> str:
    text = text.replace("\ufeff", "")
    text = text.translate(
        str.maketrans(
            {
                "’": "'",
                "‘": "'",
                "ʻ": "'",
                "ʼ": "'",
                "`": "'",
                "–": "-",
                "—": "-",
            }
        )
    )
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_question_blocks(text: str) -> list[str]:
    """Split files formatted as 'Birinchi savol ... / Javob ...'."""
    text = clean_text(text)
    blocks = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]

    # Fallback if blank lines were removed: split before every ordinal question line.
    if len(blocks) <= 1:
        pattern = re.compile(
            r"(?mi)(?=^(?:Birinchi|Ikkinchi|Uchinchi|To'rtinchi|Beshinchi|"
            r"Oltinchi|Yettinchi|Sakkizinchi|To'qqizinchi|O'ninchi|"
            r"[A-Za-z'O‘’\- ]+inchi)\s+savol\s*:)"
        )
        blocks = [block.strip() for block in pattern.split(text) if block.strip()]

    return blocks


def sentence_split(text: str) -> list[str]:
    one_line = re.sub(r"\s+", " ", text).strip()
    if not one_line:
        return []
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", one_line)
        if sentence.strip()
    ]


def chunk_text(text: str, max_chars: int = 650) -> list[str]:
    sentences = sentence_split(text)
    if not sentences:
        return []

    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        if len(sentence) > max_chars:
            words = sentence.split()
            for word in words:
                candidate = f"{current} {word}".strip()
                if current and len(candidate) > max_chars:
                    chunks.append(current)
                    current = word
                else:
                    current = candidate
            continue

        candidate = f"{current} {sentence}".strip()
        if current and len(candidate) > max_chars:
            chunks.append(current)
            current = sentence
        else:
            current = candidate

    if current:
        chunks.append(current)
    return chunks


def download_model(model_path: Path) -> None:
    if model_path.exists() and model_path.stat().st_size > 10_000_000:
        return

    model_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading the Uzbek neural voice model:\n  {model_path}")

    def report(blocks: int, block_size: int, total_size: int) -> None:
        if total_size > 0:
            percent = min(100, blocks * block_size * 100 // total_size)
            print(f"\rDownload: {percent:3d}%", end="", flush=True)

    try:
        urllib.request.urlretrieve(MODEL_URL, model_path, reporthook=report)
    except Exception:
        model_path.unlink(missing_ok=True)
        raise
    finally:
        print()


def load_model(model_path: Path):
    import torch

    torch.set_num_threads(max(1, min(8, os.cpu_count() or 4)))
    model = torch.package.PackageImporter(str(model_path)).load_pickle(
        "tts_models", "model"
    )
    model.to(torch.device("cpu"))
    return torch, model


def tensor_to_pcm16(audio) -> bytes:
    import numpy as np

    samples = audio.detach().cpu().float().flatten().numpy()
    samples = np.nan_to_num(samples, nan=0.0, posinf=1.0, neginf=-1.0)
    samples = np.clip(samples, -1.0, 1.0)
    pcm = (samples * 32767.0).astype(np.int16)
    return pcm.tobytes()


def silence_pcm(seconds: float) -> bytes:
    import numpy as np

    return np.zeros(int(SAMPLE_RATE * seconds), dtype=np.int16).tobytes()


def convert_wav_to_mp3(wav_path: Path, mp3_path: Path, speed: float) -> None:
    if not 0.5 <= speed <= 2.0:
        raise ValueError("--speed must be between 0.5 and 2.0")

    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    command = [
        ffmpeg,
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(wav_path),
        "-af",
        f"atempo={speed:.3f},loudnorm=I=-17:TP=-1.5:LRA=11",
        "-codec:a",
        "libmp3lame",
        "-b:a",
        "128k",
        str(mp3_path),
    ]
    subprocess.run(command, check=True)


def synthesize_file(
    input_path: Path,
    output_path: Path,
    torch,
    model,
    test_mode: bool,
    speed: float,
) -> None:
    text = read_text_file(input_path)
    blocks = split_question_blocks(text)
    if test_mode:
        blocks = blocks[:3]

    if not blocks:
        raise ValueError(f"No question/answer blocks found in: {input_path}")

    print(f"\nInput:  {input_path.name}")
    print(f"Blocks: {len(blocks)}")
    print(f"Output: {output_path.name}")

    with tempfile.TemporaryDirectory(prefix="uzbek_tts_") as temp_dir:
        wav_path = Path(temp_dir) / f"{input_path.stem}.wav"

        with wave.open(str(wav_path), "wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(SAMPLE_RATE)

            for block_index, block in enumerate(blocks, start=1):
                chunks = chunk_text(block)
                print(
                    f"\rSynthesizing question {block_index}/{len(blocks)}",
                    end="",
                    flush=True,
                )

                for chunk_index, chunk in enumerate(chunks):
                    with torch.inference_mode():
                        audio = model.apply_tts(
                            text=chunk,
                            speaker=SPEAKER,
                            sample_rate=SAMPLE_RATE,
                        )
                    wav_file.writeframes(tensor_to_pcm16(audio))
                    if chunk_index + 1 < len(chunks):
                        wav_file.writeframes(silence_pcm(0.18))

                wav_file.writeframes(silence_pcm(0.72))

        print()
        convert_wav_to_mp3(wav_path, output_path, speed)

    print(f"Created: {output_path}")


def main() -> int:
    args = parse_args()

    try:
        check_dependencies()
        desktop = (args.desktop or get_windows_desktop()).expanduser().resolve()
        if not desktop.exists():
            raise FileNotFoundError(f"Desktop folder not found: {desktop}")

        print(f"Desktop folder:\n  {desktop}")
        input_files = find_input_files(desktop)

        cache_dir = Path.home() / ".cache" / "uzbek_tts"
        model_path = cache_dir / MODEL_FILENAME
        download_model(model_path)
        torch, model = load_model(model_path)

        for input_path in input_files:
            suffix = "_TEST.mp3" if args.test else ".mp3"
            output_path = desktop / f"{input_path.stem}{suffix}"

            if output_path.exists() and not args.overwrite:
                print(f"Skipping existing file: {output_path.name}")
                continue

            synthesize_file(
                input_path=input_path,
                output_path=output_path,
                torch=torch,
                model=model,
                test_mode=args.test,
                speed=args.speed,
            )

        print("\nAll requested MP3 files are on the Desktop.")
        return 0

    except KeyboardInterrupt:
        print("\nCancelled by user.", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())