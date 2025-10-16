import os
import time
from typing import Tuple
import numpy as np

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, IntPrompt, FloatPrompt
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.text import Text
    from rich.align import Align
    from rich.layout import Layout
    from rich.live import Live
    from rich import box

    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Rich library not found. Install with: pip install rich")
    print("Falling back to basic terminal output...")


class MatrixCalculator:
    def __init__(self):
        if RICH_AVAILABLE:
            self.console = Console()
        else:
            self.console = None

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def print_title(self):
        """Print colorful title."""
        if self.console:
            title = Text("🔢 MATRIX CALCULATOR 🔢", style="bold magenta")
            subtitle = Text("Determinant & Rank Calculator (Max 6×6)", style="italic cyan")

            panel = Panel.fit(
                Align.center(title + "\n" + subtitle),
                box=box.DOUBLE,
                border_style="bright_blue",
                padding=(1, 2),
            )
            self.console.print(panel)
        else:
            print("=" * 50)
            print("🔢 MATRIX CALCULATOR 🔢")
            print("Determinant & Rank Calculator (Max 6×6)")
            print("=" * 50)

    def create_matrix_table(self, matrix: np.ndarray, title: str = "Matrix") -> Table:
        """Create a beautiful table representation of the matrix."""
        if not self.console:
            return None

        table = Table(
            title=f"[bold cyan]{title}[/bold cyan]",
            box=box.ROUNDED,
            border_style="bright_green",
        )

        # Add columns
        for j in range(matrix.shape[1]):
            table.add_column(f"Col {j + 1}", justify="center", style="white")

        # Add rows
        for i in range(matrix.shape[0]):
            row_data = []
            for j in range(matrix.shape[1]):
                val = matrix[i, j]
                if abs(val) < 1e-10:  # Handle near-zero values
                    val = 0

                # Color coding based on value
                if val == 0:
                    colored_val = f"[dim white]{val:8.3f}[/dim white]"
                elif val > 0:
                    colored_val = f"[green]{val:8.3f}[/green]"
                else:
                    colored_val = f"[red]{val:8.3f}[/red]"

                row_data.append(colored_val)

            table.add_row(*row_data)

        return table

    def print_matrix(self, matrix: np.ndarray, title: str = "Matrix"):
        """Print matrix with colors."""
        if self.console:
            table = self.create_matrix_table(matrix, title)
            self.console.print(table)
        else:
            print(f"\n{title}:")
            print("-" * (len(title) + 1))
            for row in matrix:
                print("[" + " ".join(f"{val:8.3f}" for val in row) + " ]")

    def show_loading(self, message: str, duration: float = 1.0):
        """Show a loading animation."""
        if self.console:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
                transient=True,
            ) as progress:
                task = progress.add_task(f"[cyan]{message}...", total=None)
                time.sleep(duration)
        else:
            print(f"{message}...")
            time.sleep(duration)

    def calculate_determinant(self, matrix: np.ndarray) -> float:
        """Calculate determinant with loading animation."""
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix must be square to calculate determinant")

        if matrix.shape[0] > 6:
            raise ValueError("Matrix size must not exceed 6x6")

        self.show_loading("Calculating determinant", 0.5)
        det = np.linalg.det(matrix)
        return det

    def calculate_rank(self, matrix: np.ndarray) -> int:
        """Calculate rank with loading animation."""
        if matrix.shape[0] > 6 or matrix.shape[1] > 6:
            raise ValueError("Matrix size must not exceed 6x6")

        self.show_loading("Calculating rank", 0.5)
        rank = np.linalg.matrix_rank(matrix)
        return rank

    def get_matrix_input(self) -> Tuple[np.ndarray, str]:
        """Get matrix input from user with improved interface."""
        if self.console:
            self.console.print("\n[bold yellow]📝 Matrix Input[/bold yellow]")

            # Get dimensions
            rows = IntPrompt.ask(
                "[cyan]Number of rows[/cyan] (1-6)", default=3, console=self.console
            )
            cols = IntPrompt.ask(
                "[cyan]Number of columns[/cyan] (1-6)", default=3, console=self.console
            )

            if rows > 6 or cols > 6 or rows < 1 or cols < 1:
                self.console.print(
                    "[bold red]❌ Error: Dimensions must be between 1 and 6[/bold red]"
                )
                raise ValueError("Invalid dimensions")

            # Get matrix elements
            matrix = np.zeros((rows, cols))
            self.console.print(f"\n[yellow]Enter elements for {rows}×{cols} matrix:[/yellow]")

            for i in range(rows):
                for j in range(cols):
                    val = FloatPrompt.ask(
                        f"[bright_white]Element[/bright_white] [{i + 1}][{j + 1}]",
                        console=self.console,
                    )
                    matrix[i, j] = val

        else:
            print("\n📝 Matrix Input")
            rows = int(input("Number of rows (1-6): "))
            cols = int(input("Number of columns (1-6): "))

            if rows > 6 or cols > 6 or rows < 1 or cols < 1:
                raise ValueError("Dimensions must be between 1 and 6")

            matrix = np.zeros((rows, cols))
            print(f"\nEnter elements for {rows}×{cols} matrix:")

            for i in range(rows):
                for j in range(cols):
                    val = float(input(f"Element [{i + 1}][{j + 1}]: "))
                    matrix[i, j] = val

        return matrix, f"{rows}×{cols}"

    def show_results(self, matrix: np.ndarray, matrix_desc: str):
        """Display calculation results with colors."""
        self.print_matrix(matrix, f"{matrix_desc} Matrix")

        try:
            # Calculate rank
            rank = self.calculate_rank(matrix)

            if self.console:
                rank_panel = Panel(
                    f"[bold green]Rank: {rank}[/bold green]",
                    border_style="green",
                    box=box.ROUNDED,
                )
                self.console.print(rank_panel)
            else:
                print(f"\n✅ Rank: {rank}")

            # Calculate determinant for square matrices
            if matrix.shape[0] == matrix.shape[1]:
                det = self.calculate_determinant(matrix)

                if self.console:
                    # Color code determinant result
                    if abs(det) < 1e-10:
                        det_color = "yellow"
                        det_text = f"Determinant: {det:.6f} (≈ 0 - Matrix is singular)"
                    elif det > 0:
                        det_color = "bright_green"
                        det_text = f"Determinant: {det:.6f}"
                    else:
                        det_color = "bright_red"
                        det_text = f"Determinant: {det:.6f}"

                    det_panel = Panel(
                        f"[bold {det_color}]{det_text}[/bold {det_color}]",
                        border_style=det_color,
                        box=box.ROUNDED,
                    )
                    self.console.print(det_panel)
                else:
                    print(f"✅ Determinant: {det:.6f}")

                # Matrix properties
                if self.console:
                    properties = []
                    if abs(det) < 1e-10:
                        properties.append("[yellow]• Singular (non-invertible)[/yellow]")
                    else:
                        properties.append("[green]• Non-singular (invertible)[/green]")

                    if rank == matrix.shape[0]:
                        properties.append("[green]• Full rank[/green]")
                    else:
                        properties.append("[yellow]• Rank deficient[/yellow]")

                    if len(properties) > 0:
                        props_text = "\n".join(properties)
                        props_panel = Panel(
                            props_text,
                            title="[bold blue]Matrix Properties[/bold blue]",
                            border_style="blue",
                            box=box.ROUNDED,
                        )
                        self.console.print(props_panel)
            else:
                if self.console:
                    self.console.print(
                        Panel(
                            "[yellow]Determinant: Not applicable (matrix is not square)[/yellow]",
                            border_style="yellow",
                            box=box.ROUNDED,
                        )
                    )
                else:
                    print("⚠️  Determinant: Not applicable (matrix is not square)")

        except Exception as e:
            if self.console:
                self.console.print(f"[bold red]❌ Error: {e}[/bold red]")
            else:
                print(f"❌ Error: {e}")

    def show_examples(self):
        """Show example calculations."""
        examples = [
            {
                "name": "2×2 Identity Matrix",
                "matrix": np.array([[1, 0], [0, 1]], dtype=float),
                "description": "Simple identity matrix",
            },
            {
                "name": "3×3 Singular Matrix",
                "matrix": np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float),
                "description": "Linear dependent rows",
            },
            {
                "name": "2×3 Rectangular Matrix",
                "matrix": np.array([[1, 2, 3], [4, 5, 6]], dtype=float),
                "description": "Non-square matrix",
            },
        ]

        if self.console:
            self.console.print(
                Panel(
                    "[bold cyan]📚 Example Calculations[/bold cyan]",
                    box=box.DOUBLE,
                    border_style="cyan",
                )
            )
        else:
            print("\n📚 Example Calculations")
            print("=" * 25)

        for i, example in enumerate(examples, 1):
            if self.console:
                self.console.print(f"\n[bold yellow]Example {i}: {example['name']}[/bold yellow]")
                self.console.print(f"[dim]{example['description']}[/dim]")
            else:
                print(f"\nExample {i}: {example['name']}")
                print(f"Description: {example['description']}")

            self.show_results(example["matrix"], f"Example {i}")

            if i < len(examples):
                if self.console:
                    self.console.print("[dim]" + "─" * 50 + "[/dim]")
                else:
                    print("-" * 30)

    def main_menu(self):
        """Main interactive menu."""
        while True:
            self.clear_screen()
            self.print_title()

            if self.console:
                menu_text = """
[bold cyan]Choose an option:[/bold cyan]

[green]1.[/green] Calculate for new matrix
[yellow]2.[/yellow] View examples  
[red]3.[/red] Exit

"""
                self.console.print(menu_text)
                choice = Prompt.ask(
                    "[bold]Your choice", choices=["1", "2", "3"], console=self.console
                )
            else:
                print("\nChoose an option:")
                print("1. Calculate for new matrix")
                print("2. View examples")
                print("3. Exit")
                choice = input("Your choice (1-3): ")

            if choice == "1":
                try:
                    matrix, desc = self.get_matrix_input()
                    self.show_results(matrix, desc)

                    if self.console:
                        Prompt.ask(
                            "\n[dim]Press Enter to continue...[/dim]",
                            default="",
                            console=self.console,
                        )
                    else:
                        input("\nPress Enter to continue...")

                except Exception as e:
                    if self.console:
                        self.console.print(f"[bold red]❌ Error: {e}[/bold red]")
                        Prompt.ask(
                            "\n[dim]Press Enter to continue...[/dim]",
                            default="",
                            console=self.console,
                        )
                    else:
                        print(f"❌ Error: {e}")
                        input("Press Enter to continue...")

            elif choice == "2":
                self.clear_screen()
                self.print_title()
                self.show_examples()

                if self.console:
                    Prompt.ask(
                        "\n[dim]Press Enter to return to main menu...[/dim]",
                        default="",
                        console=self.console,
                    )
                else:
                    input("\nPress Enter to return to main menu...")

            elif choice == "3":
                if self.console:
                    self.console.print(
                        Panel(
                            "[bold green]Thank you for using Matrix Calculator! 🎉[/bold green]",
                            border_style="green",
                            box=box.ROUNDED,
                        )
                    )
                else:
                    print("Thank you for using Matrix Calculator! 🎉")
                break


def main():
    """Main function."""
    if not RICH_AVAILABLE:
        print("\nFor the best experience, install rich library:")
        print("pip install rich numpy")
        print("\nContinuing with basic terminal output...\n")
        time.sleep(2)

    calculator = MatrixCalculator()

    try:
        calculator.main_menu()
    except KeyboardInterrupt:
        if calculator.console:
            calculator.console.print("\n[yellow]Program terminated by user. Goodbye! 👋[/yellow]")
        else:
            print("\nProgram terminated by user. Goodbye! 👋")
    except Exception as e:
        if calculator.console:
            calculator.console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
        else:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
