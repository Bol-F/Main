import math

EPS = 1e-12


def main():
    print("Square-root (Cholesky) method for solving A*x = b")

    n = int(input("Enter number of unknowns (n): "))
    if n <= 0 or n > 20:
        print("Invalid n.")
        return

    A = []
    print(f"Enter matrix A ({n} x {n}):")
    for _ in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("Invalid row length.")
            return
        A.append(row)

    b = list(map(float, input(f"Enter vector b ({n} elements):\n").split()))
    if len(b) != n:
        print("Invalid vector length.")
        return

    # --- Symmetrize A ---
    Asym = [[0.5 * (A[i][j] + A[j][i]) for j in range(n)] for i in range(n)]

    print("\nSymmetrized matrix A:")
    for i in range(n):
        print(" ".join(f"{Asym[i][j]:10.6f}" for j in range(n)))

    # --- Cholesky decomposition: Asym = L * L^T ---
    L = [[0.0] * n for _ in range(n)]
    positive_definite = True

    for i in range(n):
        for j in range(i + 1):
            sum_val = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = Asym[i][i] - sum_val
                if val <= EPS:
                    positive_definite = False
                    L[i][j] = 0.0
                else:
                    L[i][j] = math.sqrt(val)
            else:
                if abs(L[j][j]) < EPS:
                    positive_definite = False
                    L[i][j] = 0.0
                else:
                    L[i][j] = (Asym[i][j] - sum_val) / L[j][j]

    if not positive_definite:
        print("\nMatrix is not positive-definite. Cholesky decomposition failed.")
        return

    print("\nLower-triangular matrix L:")
    for i in range(n):
        print(" ".join(f"{L[i][j]:10.6f}" if j <= i else f"{0.0:10.6f}" for j in range(n)))

    # --- Forward substitution: L*y = b ---
    y = [0.0] * n
    for i in range(n):
        sum_val = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_val) / L[i][i]

    # --- Back substitution: L^T*x = y ---
    x = [0.0] * n
    for i in reversed(range(n)):
        sum_val = sum(L[j][i] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_val) / L[i][i]

    # --- Determinant ---
    det = 1.0
    for i in range(n):
        det *= L[i][i]
    det = det * det

    print("\nSolution vector X:")
    for i in range(n):
        print(f"x[{i + 1}] = {x[i]:.6f}")

    print(f"\nDeterminant of A: {det:.6f}")


if __name__ == "__main__":
    main()
