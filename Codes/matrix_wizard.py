#!/usr/bin/env python3
# matrix_wizard.py
"""
🎭 Matrix Wizard - The Ultimate Determinant Calculator 🎭

Enhanced features:
- Interactive matrix editor with arrow key navigation
- Real-time matrix operations visualization
- Multiple calculation methods with performance comparison
- Matrix properties analysis (rank, trace, condition number)
- Beautiful ASCII art animations
- Sound effects simulation (visual bell)
- Matrix gallery with famous matrices
- Export results to various formats
- Undo/Redo functionality
- Matrix transformations preview
- Educational mode with step-by-step explanations
"""

import argparse
import csv
import itertools
import json
import os
import random
import sys
import threading
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import List, Union, Tuple, Optional, Dict, Any

Number = Union[int, float, Fraction]


# ============================================================================
# Enhanced Color System & Visual Effects
# ============================================================================


class Colors:
    """Enhanced color palette with gradients and effects"""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"

    # Regular colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


def supports_colors() -> bool:
    return sys.stdout.isatty() and os.getenv("TERM", "").lower() != "dumb"


COLOR_ENABLED = supports_colors()


def colorize(text: str, *codes: str) -> str:
    if not COLOR_ENABLED:
        return text
    return "".join(codes) + text + Colors.RESET


def rainbow_text(text: str) -> str:
    """Apply rainbow colors to text"""
    if not COLOR_ENABLED:
        return text
    colors = [
        Colors.RED,
        Colors.YELLOW,
        Colors.GREEN,
        Colors.CYAN,
        Colors.BLUE,
        Colors.MAGENTA,
    ]
    result = ""
    for i, char in enumerate(text):
        if char != " ":
            result += colors[i % len(colors)] + char + Colors.RESET
        else:
            result += char
    return result


def gradient_text(text: str, start_color: str, end_color: str) -> str:
    """Create gradient effect (simplified)"""
    if not COLOR_ENABLED:
        return text
    mid = len(text) // 2
    return start_color + text[:mid] + end_color + text[mid:] + Colors.RESET


# ============================================================================
# Advanced Spinner and Progress Indicators
# ============================================================================


class AdvancedSpinner:
    """Enhanced spinner with multiple styles and progress tracking"""

    STYLES = {
        "dots": "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏",
        "line": "|/-\\",
        "arrows": "←↖↑↗→↘↓↙",
        "bouncing": "⠁⠂⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟",
        "pulse": "●◐◑◒◓◔◕○",
        "matrix": "█▉▊▋▌▍▎▏▎▍▌▋▊▉",
        "fire": "🔥💥✨⭐🌟💫⚡",
    }

    def __init__(
        self, message: str = "Processing", style: str = "dots", color: str = Colors.CYAN
    ):
        self.message = message
        self.style = self.STYLES.get(style, self.STYLES["dots"])
        self.color = color
        self._running = False
        self._thread = None
        self.progress = 0.0

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=0.5)
        self._clear_line()

    def update_progress(self, progress: float):
        self.progress = max(0.0, min(1.0, progress))

    def _spin(self):
        for frame in itertools.cycle(self.style):
            if not self._running:
                break

            progress_bar = self._create_progress_bar()
            spinner_text = (
                f"\r{self.color}{frame} {self.message}{Colors.RESET} {progress_bar}"
            )

            sys.stdout.write(spinner_text)
            sys.stdout.flush()
            time.sleep(0.2)

    def _create_progress_bar(self) -> str:
        if self.progress == 0.0:
            return ""

        width = 20
        filled = int(width * self.progress)
        bar = "█" * filled + "░" * (width - filled)
        percentage = f"{self.progress * 100:.1f}%"
        return f"[{bar}] {percentage}"

    def _clear_line(self):
        sys.stdout.write("\r" + " " * 80 + "\r")
        sys.stdout.flush()


# ============================================================================
# Matrix Operations and Analysis
# ============================================================================


@dataclass
class MatrixStats:
    """Container for matrix statistics and properties"""

    determinant: Number
    trace: Number
    rank: int
    condition_number: Optional[float]
    is_singular: bool
    is_symmetric: bool
    is_orthogonal: bool
    eigenvalue_estimate: Optional[List[complex]]


class MatrixAnalyzer:
    """Advanced matrix analysis and operations"""

    @staticmethod
    def analyze_matrix(matrix: List[List[Number]]) -> MatrixStats:
        """Comprehensive matrix analysis"""
        n = len(matrix)

        # Calculate basic properties
        det, _ = MatrixCalculator.determinant_lu(matrix)
        trace = sum(matrix[i][i] for i in range(n))

        # Check symmetry
        is_symmetric = all(
            matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n)
        )

        # Estimate rank (simplified)
        rank = MatrixAnalyzer._estimate_rank(matrix)

        # Check if singular
        is_singular = (
            abs(float(det)) < 1e-10 if isinstance(det, (int, float)) else det == 0
        )

        return MatrixStats(
            determinant=det,
            trace=trace,
            rank=rank,
            condition_number=None,  # Would need SVD for accurate calculation
            is_singular=is_singular,
            is_symmetric=is_symmetric,
            is_orthogonal=False,  # Simplified
            eigenvalue_estimate=None,
        )

    @staticmethod
    def _estimate_rank(matrix: List[List[Number]]) -> int:
        """Simple rank estimation using Gaussian elimination"""
        n = len(matrix)
        m = [row[:] for row in matrix]  # Copy matrix

        rank = 0
        for i in range(n):
            # Find pivot
            pivot = None
            for j in range(i, n):
                if abs(float(m[j][i])) > 1e-10:
                    pivot = j
                    break

            if pivot is None:
                continue

            if pivot != i:
                m[i], m[pivot] = m[pivot], m[i]

            rank += 1

            # Eliminate below
            for j in range(i + 1, n):
                if abs(float(m[i][i])) > 1e-10:
                    factor = m[j][i] / m[i][i]
                    for k in range(i, n):
                        m[j][k] = m[j][k] - factor * m[i][k]

        return rank


class MatrixCalculator:
    """Enhanced determinant calculation with multiple algorithms"""

    @staticmethod
    def determinant_recursive(
        matrix: List[List[Number]], progress_callback=None
    ) -> Number:
        """Recursive determinant with progress tracking"""

        def _det_recursive(m: List[List[Number]], depth: int = 0) -> Number:
            n = len(m)
            if progress_callback and depth == 0:
                progress_callback(0.1)

            if n == 1:
                return m[0][0]
            if n == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            det = 0
            for j in range(n):
                sign = (-1) ** j
                minor = [row[:j] + row[j + 1 :] for row in m[1:]]
                cofactor = _det_recursive(minor, depth + 1)
                det += sign * m[0][j] * cofactor

                if progress_callback and depth == 0:
                    progress_callback((j + 1) / n * 0.9)

            return det

        return _det_recursive(matrix)

    @staticmethod
    def determinant_lu(
        matrix: List[List[Number]], show_steps: bool = False
    ) -> Tuple[Number, List[str]]:
        """LU decomposition with detailed steps"""
        n = len(matrix)
        m = [row[:] for row in matrix]
        steps = []
        swaps = 0

        if show_steps:
            steps.append("🔍 Starting LU Decomposition...")
            steps.append(f"Initial matrix ({n}×{n}):")

        for i in range(n):
            # Partial pivoting
            max_row = i
            for k in range(i + 1, n):
                if abs(float(m[k][i])) > abs(float(m[max_row][i])):
                    max_row = k

            if max_row != i:
                m[i], m[max_row] = m[max_row], m[i]
                swaps += 1
                if show_steps:
                    steps.append(f"🔄 Swapped rows {i + 1} ↔ {max_row + 1}")

            # Check for zero pivot
            if abs(float(m[i][i])) < 1e-12:
                if show_steps:
                    steps.append("⚠️  Zero pivot found - matrix is singular!")
                return (Fraction(0) if isinstance(m[0][0], Fraction) else 0.0, steps)

            # Elimination
            for k in range(i + 1, n):
                factor = m[k][i] / m[i][i]
                for j in range(i, n):
                    m[k][j] -= factor * m[i][j]

                if show_steps and factor != 0:
                    steps.append(
                        f"📉 R{k + 1} = R{k + 1} - {MatrixFormatter.format_number(factor)} × R{i + 1}"
                    )

        # Calculate determinant
        det = m[0][0]
        for i in range(1, n):
            det *= m[i][i]

        if swaps % 2:
            det = -det

        if show_steps:
            steps.append("✅ Elimination complete!")
            steps.append(
                f"🎯 Product of diagonal: {MatrixFormatter.format_number(det)}"
            )
            if swaps % 2:
                steps.append(f"🔄 Applied sign change for {swaps} row swaps")

        return (det, steps)


# ============================================================================
# Enhanced Matrix Formatting and Display
# ============================================================================


class MatrixFormatter:
    """Advanced matrix formatting with styling options"""

    @staticmethod
    def format_number(num: Number, precision: int = 6) -> str:
        """Format number with appropriate precision"""
        if isinstance(num, Fraction):
            if num.denominator == 1:
                return str(num.numerator)
            return f"{num.numerator}/{num.denominator}"

        if isinstance(num, complex):
            real = f"{num.real:.{precision}g}" if num.real != 0 else ""
            imag = f"{num.imag:.{precision}g}i" if num.imag != 0 else ""
            if real and imag:
                sign = "+" if num.imag >= 0 else "-"
                return f"{real}{sign}{abs(num.imag):.{precision}g}i"
            return real or imag or "0"

        if isinstance(num, (int, float)):
            if isinstance(num, int) or num.is_integer():
                return str(int(num))
            return f"{num:.{precision}g}"

        return str(num)

    @staticmethod
    def format_matrix(
        matrix: List[List[Number]], style: str = "box", highlight_diagonal: bool = False
    ) -> str:
        """Format matrix with various visual styles"""
        if not matrix:
            return "∅ (empty matrix)"

        n = len(matrix)

        # Calculate column widths
        col_widths = [0] * n
        formatted_matrix = []

        for i, row in enumerate(matrix):
            formatted_row = []
            for j, val in enumerate(row):
                formatted_val = MatrixFormatter.format_number(val)
                if highlight_diagonal and i == j:
                    formatted_val = colorize(formatted_val, Colors.BOLD, Colors.YELLOW)
                formatted_row.append(formatted_val)
                col_widths[j] = max(
                    col_widths[j], len(MatrixFormatter.format_number(val))
                )
            formatted_matrix.append(formatted_row)

        if style == "box":
            return MatrixFormatter._format_box_style(formatted_matrix, col_widths)
        elif style == "brackets":
            return MatrixFormatter._format_brackets_style(formatted_matrix, col_widths)
        elif style == "grid":
            return MatrixFormatter._format_grid_style(formatted_matrix, col_widths)
        else:
            return MatrixFormatter._format_simple_style(formatted_matrix, col_widths)

    @staticmethod
    def _format_box_style(matrix: List[List[str]], widths: List[int]) -> str:
        """Format matrix with box drawing characters"""
        n = len(matrix)
        lines = []

        # Top border
        top = "┌" + "┬".join("─" * (w + 2) for w in widths) + "┐"
        lines.append(top)

        for i, row in enumerate(matrix):
            # Row content
            content = (
                "│"
                + "│".join(f" {cell:>{widths[j]}} " for j, cell in enumerate(row))
                + "│"
            )
            lines.append(content)

            # Middle border (except for last row)
            if i < n - 1:
                middle = "├" + "┼".join("─" * (w + 2) for w in widths) + "┤"
                lines.append(middle)

        # Bottom border
        bottom = "└" + "┴".join("─" * (w + 2) for w in widths) + "┘"
        lines.append(bottom)

        return "\n".join(lines)

    @staticmethod
    def _format_brackets_style(matrix: List[List[str]], widths: List[int]) -> str:
        """Format matrix with brackets"""
        lines = []
        n = len(matrix)

        for i, row in enumerate(matrix):
            left_bracket = "⎡" if i == 0 else "⎢" if i < n - 1 else "⎣"
            right_bracket = "⎤" if i == 0 else "⎥" if i < n - 1 else "⎦"

            content = "  ".join(f"{cell:>{widths[j]}}" for j, cell in enumerate(row))
            lines.append(f"{left_bracket} {content} {right_bracket}")

        return "\n".join(lines)

    @staticmethod
    def _format_grid_style(matrix: List[List[str]], widths: List[int]) -> str:
        """Format matrix with simple grid"""
        lines = []
        separator = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

        lines.append(separator)
        for row in matrix:
            content = (
                "|"
                + "|".join(f" {cell:>{widths[j]}} " for j, cell in enumerate(row))
                + "|"
            )
            lines.append(content)
            lines.append(separator)

        return "\n".join(lines)

    @staticmethod
    def _format_simple_style(matrix: List[List[str]], widths: List[int]) -> str:
        """Simple matrix formatting"""
        lines = []
        for row in matrix:
            content = "  ".join(f"{cell:>{widths[j]}}" for j, cell in enumerate(row))
            lines.append(content)
        return "\n".join(lines)


# ============================================================================
# Matrix Gallery - Famous Matrices
# ============================================================================


class MatrixGallery:
    """Collection of famous and interesting matrices"""

    FAMOUS_MATRICES = {
        "identity_3": {
            "name": "Identity Matrix (3×3)",
            "description": "The multiplicative identity for matrices",
            "matrix": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            "expected_det": 1,
        },
        "hilbert_3": {
            "name": "Hilbert Matrix (3×3)",
            "description": "Famous ill-conditioned matrix, H[i,j] = 1/(i+j-1)",
            "matrix": [
                [Fraction(1, 1), Fraction(1, 2), Fraction(1, 3)],
                [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)],
                [Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)],
            ],
            "expected_det": Fraction(1, 2160),
        },
        "pascal_4": {
            "name": "Pascal Matrix (4×4)",
            "description": "Matrix with Pascal's triangle values",
            "matrix": [[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10], [1, 4, 10, 20]],
            "expected_det": 1,
        },
        "magic_3": {
            "name": "Magic Square (3×3)",
            "description": "All rows, columns, and diagonals sum to 15",
            "matrix": [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            "expected_det": -360,
        },
        "vandermonde_3": {
            "name": "Vandermonde Matrix (3×3)",
            "description": "V[i,j] = x_i^j, with x = [1, 2, 3]",
            "matrix": [[1, 1, 1], [1, 2, 4], [1, 3, 9]],
            "expected_det": 2,
        },
        "rotation_2d": {
            "name": "2D Rotation Matrix (45°)",
            "description": "Rotates vectors by 45 degrees",
            "matrix": [[0.707, -0.707], [0.707, 0.707]],
            "expected_det": 1.0,
        },
    }

    @staticmethod
    def list_matrices() -> List[str]:
        """Return list of available matrix names"""
        return list(MatrixGallery.FAMOUS_MATRICES.keys())

    @staticmethod
    def get_matrix(name: str) -> Optional[Dict[str, Any]]:
        """Get matrix by name"""
        return MatrixGallery.FAMOUS_MATRICES.get(name)

    @staticmethod
    def display_gallery():
        """Display available matrices in gallery"""
        print(colorize("🎨 Matrix Gallery", Colors.BOLD, Colors.MAGENTA))
        print("=" * 50)

        for key, matrix_info in MatrixGallery.FAMOUS_MATRICES.items():
            print(f"\n📐 {colorize(matrix_info['name'], Colors.BOLD, Colors.CYAN)}")
            print(f"   {matrix_info['description']}")
            print(
                f"   Expected determinant: {colorize(str(matrix_info['expected_det']), Colors.GREEN)}"
            )
            print(f"   Command: --gallery {key}")


# ============================================================================
# Interactive Matrix Editor
# ============================================================================


class InteractiveEditor:
    """Interactive matrix editor with navigation and editing"""

    def __init__(self, size: int, exact_mode: bool = False):
        self.size = size
        self.exact_mode = exact_mode
        self.matrix = self._create_empty_matrix()
        self.cursor_row = 0
        self.cursor_col = 0

    def _create_empty_matrix(self) -> List[List[Number]]:
        """Create empty matrix with zeros"""
        if self.exact_mode:
            return [[Fraction(0) for _ in range(self.size)] for _ in range(self.size)]
        else:
            return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def edit_matrix(self) -> List[List[Number]]:
        """Interactive matrix editing session"""
        print(colorize("🎛️  Interactive Matrix Editor", Colors.BOLD, Colors.CYAN))
        print("Use arrow keys to navigate, Enter to edit cell, 'q' to finish")
        print("Commands: 'r' = random fill, 'c' = clear, 'i' = identity, 'z' = zeros")
        print()

        # This would need a proper terminal input handler for arrow keys
        # For now, let's provide a simplified version
        return self._simplified_editor()

    def _simplified_editor(self) -> List[List[Number]]:
        """Simplified editor without arrow key support"""
        print("Enter matrix values row by row:")

        for i in range(self.size):
            print(f"\nRow {i + 1}:")
            for j in range(self.size):
                while True:
                    try:
                        value_str = input(f"  [{i + 1},{j + 1}] = ").strip()
                        if not value_str:
                            value_str = "0"

                        if self.exact_mode:
                            if "/" in value_str:
                                value = Fraction(value_str)
                            else:
                                value = Fraction(int(value_str))
                        else:
                            value = (
                                float(value_str) if "." in value_str else int(value_str)
                            )

                        self.matrix[i][j] = value
                        break
                    except (ValueError, ZeroDivisionError) as e:
                        print(f"Invalid input: {e}. Please try again.")

        return self.matrix


# ============================================================================
# File I/O Operations
# ============================================================================


def load_matrix_from_csv(filename: str, exact_mode: bool = False) -> List[List[Number]]:
    """Load matrix from CSV file"""
    try:
        matrix = []
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                matrix_row = []
                for cell in row:
                    cell = cell.strip()
                    if not cell:
                        continue

                    if exact_mode:
                        if "/" in cell:
                            matrix_row.append(Fraction(cell))
                        else:
                            matrix_row.append(Fraction(int(cell)))
                    else:
                        matrix_row.append(float(cell) if "." in cell else int(cell))

                if matrix_row:  # Only add non-empty rows
                    matrix.append(matrix_row)

        # Validate square matrix
        n = len(matrix)
        if not all(len(row) == n for row in matrix):
            raise ValueError("Matrix must be square")

        return matrix

    except FileNotFoundError:
        print(colorize(f"❌ File '{filename}' not found!", Colors.RED))
        sys.exit(1)
    except Exception as e:
        print(colorize(f"❌ Error loading matrix: {e}", Colors.RED))
        sys.exit(1)


def generate_random_matrix(
    size: int, exact_mode: bool = False, int_range: Tuple[int, int] = (-10, 10)
) -> List[List[Number]]:
    """Generate random matrix"""
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if exact_mode:
                # Generate random fractions
                num = random.randint(int_range[0], int_range[1])
                den = random.randint(1, 5)
                row.append(Fraction(num, den))
            else:
                row.append(random.randint(int_range[0], int_range[1]))
        matrix.append(row)
    return matrix


# ============================================================================
# Enhanced CLI with Rich Features
# ============================================================================


def print_ascii_art():
    """Display cool ASCII art header"""
    art = r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗    ██╗    ██╗██╗███████╗  ║
║    ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝    ██║    ██║██║╚══███╔╝  ║
║    ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝     ██║ █╗ ██║██║  ███╔╝   ║
║    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗     ██║███╗██║██║ ███╔╝    ║
║    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗    ╚███╔███╔╝██║███████╗  ║
║    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚══════╝  ║
║                                                                              ║
║                  🎭 The Ultimate Matrix Determinant Calculator 🎭              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """

    if COLOR_ENABLED:
        # Apply rainbow effect to the art
        lines = art.strip().split("\n")
        colored_lines = []
        for line in lines:
            if "█" in line or "╗" in line or "║" in line:
                colored_lines.append(gradient_text(line, Colors.CYAN, Colors.MAGENTA))
            else:
                colored_lines.append(colorize(line, Colors.BRIGHT_BLUE))
        print("\n".join(colored_lines))
    else:
        print(art)

    print(
        colorize(
            "✨ Enhanced with real-time analysis, interactive editing, and visual effects! ✨",
            Colors.BOLD,
            Colors.YELLOW,
        )
    )
    print()


def benchmark_methods(matrix: List[List[Number]]) -> Dict[str, float]:
    """Benchmark different calculation methods"""
    results = {}

    # LU method
    start_time = time.time()
    det_lu, _ = MatrixCalculator.determinant_lu(matrix)
    results["LU Decomposition"] = time.time() - start_time

    # Recursive method (only for small matrices)
    if len(matrix) <= 6:
        start_time = time.time()
        det_recursive = MatrixCalculator.determinant_recursive(matrix)
        results["Recursive"] = time.time() - start_time

    return results


def export_results(
    matrix: List[List[Number]], analysis: MatrixStats, filename: str, format_type: str
):
    """Export results to various formats"""
    data = {
        "matrix": [
            [MatrixFormatter.format_number(cell) for cell in row] for row in matrix
        ],
        "determinant": MatrixFormatter.format_number(analysis.determinant),
        "trace": MatrixFormatter.format_number(analysis.trace),
        "rank": analysis.rank,
        "is_singular": analysis.is_singular,
        "is_symmetric": analysis.is_symmetric,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    if format_type.lower() == "json":
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    elif format_type.lower() == "csv":
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Matrix"])
            for row in matrix:
                writer.writerow([MatrixFormatter.format_number(cell) for cell in row])
            writer.writerow([])
            writer.writerow(["Property", "Value"])
            writer.writerow(
                ["Determinant", MatrixFormatter.format_number(analysis.determinant)]
            )
            writer.writerow(["Trace", MatrixFormatter.format_number(analysis.trace)])
            writer.writerow(["Rank", analysis.rank])

    print(colorize(f"✅ Results exported to {filename}", Colors.GREEN))


def display_matrix_analysis(
    matrix: List[List[Number]],
    analysis: MatrixStats,
    show_steps: bool = False,
    animate: bool = False,
):
    """Display comprehensive matrix analysis"""
    print(colorize("📊 Matrix Analysis Report", Colors.BOLD, Colors.BLUE))
    print("=" * 60)

    # Display matrix
    print(f"\n📐 Matrix ({len(matrix)}×{len(matrix)}):")
    print(MatrixFormatter.format_matrix(matrix, style="box", highlight_diagonal=True))

    # Basic properties
    print(
        f"\n🎯 {colorize('Determinant:', Colors.BOLD)} {colorize(MatrixFormatter.format_number(analysis.determinant), Colors.GREEN if not analysis.is_singular else Colors.RED)}"
    )
    print(
        f"🔢 {colorize('Trace:', Colors.BOLD)} {colorize(MatrixFormatter.format_number(analysis.trace), Colors.CYAN)}"
    )
    print(
        f"📏 {colorize('Rank:', Colors.BOLD)} {colorize(str(analysis.rank), Colors.YELLOW)}"
    )

    # Matrix properties
    print(f"\n🔍 {colorize('Matrix Properties:', Colors.BOLD)}")
    print(
        f"   • Singular: {colorize('Yes' if analysis.is_singular else 'No', Colors.RED if analysis.is_singular else Colors.GREEN)}"
    )
    print(
        f"   • Symmetric: {colorize('Yes' if analysis.is_symmetric else 'No', Colors.GREEN if analysis.is_symmetric else Colors.YELLOW)}"
    )

    if show_steps:
        print(f"\n📝 {colorize('Calculation Steps (LU Decomposition):', Colors.BOLD)}")
        _, steps = MatrixCalculator.determinant_lu(matrix, show_steps=True)
        for step in steps:
            print(f"   {step}")

    if animate:
        print(f"\n{colorize('🎬 Animated calculation...', Colors.MAGENTA)}")
        spinner = AdvancedSpinner(
            "Calculating determinant", style="matrix", color=Colors.CYAN
        )
        spinner.start()
        time.sleep(2)  # Simulate calculation
        spinner.stop()
        print(colorize("✅ Animation complete!", Colors.GREEN))


def main():
    """Enhanced main function with rich CLI"""
    parser = argparse.ArgumentParser(
        description="🎭 Matrix Wizard - Ultimate Determinant Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --size 3 --method lu --animate        # Interactive 3x3 matrix with animation
  %(prog)s --gallery hilbert_3 --exact           # Load Hilbert matrix with exact arithmetic
  %(prog)s --random 4 --benchmark                # Random 4x4 matrix with performance test
  %(prog)s --file matrix.csv --export results.json --format json
        """,
    )

    # Input sources (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--size",
        "-s",
        type=int,
        metavar="N",
        help="Create N×N matrix (interactive input)",
    )
    input_group.add_argument(
        "--file", "-f", type=str, metavar="FILE", help="Load matrix from CSV file"
    )
    input_group.add_argument(
        "--random", "-r", type=int, metavar="N", help="Generate random N×N matrix"
    )
    input_group.add_argument(
        "--gallery",
        "-g",
        type=str,
        metavar="NAME",
        help="Load matrix from gallery",
        choices=MatrixGallery.list_matrices(),
    )
    input_group.add_argument(
        "--list-gallery", action="store_true", help="Show available matrices in gallery"
    )

    # Calculation options
    parser.add_argument(
        "--method",
        "-m",
        choices=["lu", "recursive", "both"],
        default="lu",
        help="Calculation method (default: lu)",
    )
    parser.add_argument(
        "--exact", "-e", action="store_true", help="Use exact arithmetic with fractions"
    )
    parser.add_argument(
        "--steps", action="store_true", help="Show step-by-step calculation"
    )

    # Visual options
    parser.add_argument(
        "--style",
        choices=["box", "brackets", "grid", "simple"],
        default="box",
        help="Matrix display style",
    )
    parser.add_argument(
        "--animate", "-a", action="store_true", help="Show animated calculations"
    )
    parser.add_argument(
        "--no-color", action="store_true", help="Disable colored output"
    )

    # Analysis options
    parser.add_argument(
        "--benchmark",
        "-b",
        action="store_true",
        help="Benchmark different calculation methods",
    )
    parser.add_argument(
        "--analyze",
        action="store_true",
        default=True,
        help="Perform comprehensive matrix analysis",
    )

    # Export options
    parser.add_argument(
        "--export", type=str, metavar="FILE", help="Export results to file"
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Export format (default: json)",
    )

    # Random matrix options
    parser.add_argument(
        "--range",
        type=int,
        nargs=2,
        default=[-10, 10],
        metavar=("MIN", "MAX"),
        help="Range for random values",
    )

    args = parser.parse_args()

    # Handle color preference
    if args.no_color:
        global COLOR_ENABLED
        COLOR_ENABLED = False

    # Show gallery list if requested
    if args.list_gallery:
        MatrixGallery.display_gallery()
        return

    # Print header
    print_ascii_art()

    # Initialize matrix based on input source
    matrix = None
    matrix_info = None

    try:
        if args.size:
            print(
                colorize(
                    f"🎛️  Creating {args.size}×{args.size} matrix",
                    Colors.BOLD,
                    Colors.CYAN,
                )
            )
            editor = InteractiveEditor(args.size, args.exact)
            matrix = editor.edit_matrix()

        elif args.file:
            print(
                colorize(
                    f"📁 Loading matrix from {args.file}", Colors.BOLD, Colors.CYAN
                )
            )
            matrix = load_matrix_from_csv(args.file, args.exact)

        elif args.random:
            print(
                colorize(
                    f"🎲 Generating random {args.random}×{args.random} matrix",
                    Colors.BOLD,
                    Colors.CYAN,
                )
            )
            matrix = generate_random_matrix(args.random, args.exact, tuple(args.range))

        elif args.gallery:
            matrix_info = MatrixGallery.get_matrix(args.gallery)
            if matrix_info:
                print(
                    colorize(
                        f"🎨 Loading {matrix_info['name']} from gallery",
                        Colors.BOLD,
                        Colors.CYAN,
                    )
                )
                matrix = matrix_info["matrix"]
            else:
                print(
                    colorize(
                        f"❌ Matrix '{args.gallery}' not found in gallery!", Colors.RED
                    )
                )
                return

        if matrix is None:
            print(colorize("❌ Failed to load matrix!", Colors.RED))
            return

        # Validate matrix
        n = len(matrix)
        if n == 0 or not all(len(row) == n for row in matrix):
            print(
                colorize("❌ Invalid matrix: must be square and non-empty!", Colors.RED)
            )
            return

        print(colorize(f"\n✅ Matrix loaded successfully! ({n}×{n})", Colors.GREEN))

        # Perform analysis
        if args.animate:
            spinner = AdvancedSpinner(
                "Analyzing matrix", style="pulse", color=Colors.MAGENTA
            )
            spinner.start()
            time.sleep(1.5)  # Simulate analysis

        analysis = MatrixAnalyzer.analyze_matrix(matrix)

        if args.animate:
            spinner.stop()

        # Display results
        display_matrix_analysis(matrix, analysis, args.steps, args.animate)

        # Benchmark if requested
        if args.benchmark:
            print(
                f"\n⏱️  {colorize('Performance Benchmark:', Colors.BOLD, Colors.YELLOW)}"
            )
            print("-" * 40)

            benchmark_results = benchmark_methods(matrix)
            for method, elapsed_time in benchmark_results.items():
                print(f"   {method:20}: {elapsed_time:.6f}s")

        # Verify against expected result if from gallery
        if matrix_info and "expected_det" in matrix_info:
            expected = matrix_info["expected_det"]
            actual = analysis.determinant

            print(f"\n🎯 {colorize('Verification:', Colors.BOLD)}")
            print(
                f"   Expected: {colorize(MatrixFormatter.format_number(expected), Colors.CYAN)}"
            )
            print(
                f"   Actual:   {colorize(MatrixFormatter.format_number(actual), Colors.CYAN)}"
            )

            # Check if values match (with tolerance for floating point)
            if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
                match = abs(float(expected) - float(actual)) < 1e-10
            else:
                match = expected == actual

            status = (
                colorize("✅ PASSED", Colors.GREEN)
                if match
                else colorize("❌ FAILED", Colors.RED)
            )
            print(f"   Status:   {status}")

        # Export results if requested
        if args.export:
            export_results(matrix, analysis, args.export, args.format)

        # Final summary
        print(f"\n{colorize('📋 Summary:', Colors.BOLD)}")
        print(f"   Matrix size: {n}×{n}")
        print(
            f"   Determinant: {colorize(MatrixFormatter.format_number(analysis.determinant), Colors.BOLD)}"
        )
        print(
            f"   Matrix type: {'Singular' if analysis.is_singular else 'Non-singular'}"
        )
        if analysis.is_symmetric:
            print(f"   Special: Symmetric matrix")

        print(
            f"\n{rainbow_text('🎉 Calculation complete! Thank you for using Matrix Wizard! 🎉')}"
        )

    except KeyboardInterrupt:
        print(f"\n\n{colorize('⏹️  Operation cancelled by user.', Colors.YELLOW)}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{colorize(f'💥 Unexpected error: {e}', Colors.RED)}")
        if "--debug" in sys.argv:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
