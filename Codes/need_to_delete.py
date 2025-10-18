import numpy as np

np.set_printoptions(precision=6, suppress=True)


def build_system(V):
    A = np.array([
        [V + 1, V + 2, -V, 4 * V, -V],
        [V + 4, -2 * V, 3 * V, -V, 4 * V],
        [V + 2, V + 4, -V + 1, V + 1, -V + 3],
        [V + 3, V + 5, -V + 1, V + 2, -V + 4],
        [V, V + 1, V + 2, V + 3, V + 4]
    ], dtype=float)

    b = np.array([
        4 * V ** 2 + 6 * V + 4,
        5 * V ** 2 + 24 * V + 16,
        V ** 2 + 3 * V,
        V ** 2 + 5 * V + 3,
        5 * V ** 2 + 20 * V + 17
    ], dtype=float)

    return A, b


def ldlt_decomposition(A, tol=1e-12):
    """LDL^T decomposition. Returns L (unit lower), D (1D array). Raises ValueError if small pivot."""
    n = A.shape[0]
    L = np.eye(n, dtype=float)
    D = np.zeros(n, dtype=float)

    for i in range(n):
        s = 0.0
        for k in range(i):
            s += (L[i, k] ** 2) * D[k]
        D[i] = A[i, i] - s

        if abs(D[i]) < tol:
            raise ValueError(f"Small pivot D[{i}] = {D[i]:.3e}")

        for j in range(i + 1, n):
            s2 = 0.0
            for k in range(i):
                s2 += L[j, k] * L[i, k] * D[k]
            L[j, i] = (A[j, i] - s2) / D[i]

    return L, D


def solve_ldlt(L, D, b):
    # Solve L y = b
    n = len(b)
    y = np.zeros(n, dtype=float)
    for i in range(n):
        s = 0.0
        for k in range(i):
            s += L[i, k] * y[k]
        y[i] = b[i] - s

    # D z = y
    z = y / D

    # L^T x = z
    x = np.zeros(n, dtype=float)
    for i in reversed(range(n)):
        s = 0.0
        for k in range(i + 1, n):
            s += L[k, i] * x[k]  # since (L^T)[i,k] = L[k,i]
        x[i] = z[i] - s

    return x, y, z


def is_symmetric(A, tol=1e-9):
    return np.allclose(A, A.T, atol=tol, rtol=0)


def is_positive_definite_cholesky(A):
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False


def eigen_positive_definite(A, tol=1e-10):
    vals = np.linalg.eigvalsh(A)  # symmetric faster routine
    return vals, np.all(vals > tol)


def main():
    try:
        V = int(input("Enter value of V: ").strip())
    except Exception:
        print("Нужно целое число V. Выход.")
        return

    # Build original system
    A_original, b = build_system(V)

    print("\n=== ИСХОДНАЯ МАТРИЦА A ===")
    print(A_original)

    # Answer questions about ORIGINAL matrix
    print("\n=== ОТВЕТЫ НА ВОПРОСЫ ДЛЯ ИСХОДНОЙ МАТРИЦЫ ===")

    # 1. Determinant
    det_original = np.linalg.det(A_original)
    is_zero_original = abs(det_original) < 1e-9
    print(f"1. Детерминант матрицы A: {det_original:.6g}")
    print(f"   Детерминант равен нулю? {'ДА' if is_zero_original else 'НЕТ'}")

    # 2. Symmetry
    sym_original = is_symmetric(A_original)
    print(f"2. Симметричная ли матрица? {'ДА' if sym_original else 'НЕТ'}")

    # 3. Positive definite
    pd_cholesky_original = is_positive_definite_cholesky(A_original)
    eigs_original, pd_eigs_original = eigen_positive_definite(A_original)
    print(f"3. Положительно определённая ли матрица? {'ДА' if pd_cholesky_original else 'НЕТ'}")

    # Check if any answer is NO
    any_no = is_zero_original or (not sym_original) or (not pd_cholesky_original)

    if any_no:
        print(f"\n=== Т.к. на один из вопросов ответ 'НЕТ', применяем СИММЕТРИЗАЦИЮ СИСТЕМЫ ===")

        # Symmetrize the matrix
        A_sym = 0.5 * (A_original + A_original.T)

        print("\nСимметризованная матрица A_sym:")
        print(A_sym)

        # Answer questions for symmetrized matrix
        print("\n=== ОТВЕТЫ НА ВОПРОСЫ ДЛЯ СИММЕТРИЗОВАННОЙ МАТРИЦЫ ===")

        # 1. Determinant
        det_sym = np.linalg.det(A_sym)
        is_zero_sym = abs(det_sym) < 1e-9
        print(f"1. Детерминант матрицы A_sym: {det_sym:.6g}")
        print(f"   Детерминант равен нулю? {'ДА' if is_zero_sym else 'НЕТ'}")

        # 2. Symmetry (should always be YES after symmetrization)
        sym_sym = is_symmetric(A_sym)
        print(f"2. Симметричная ли матрица? {'ДА' if sym_sym else 'НЕТ'}")

        # 3. Positive definite
        pd_cholesky_sym = is_positive_definite_cholesky(A_sym)
        eigs_sym, pd_eigs_sym = eigen_positive_definite(A_sym)
        print(f"3. Положительно определённая ли матрица? {'ДА' if pd_cholesky_sym else 'НЕТ'}")

        # Use symmetrized matrix for further calculations
        A_to_use = A_sym
        print(f"\nИспользуем симметризованную матрицу для дальнейших вычислений")

    else:
        print(f"\n=== Все ответы 'ДА', используем исходную матрицу ===")
        A_to_use = A_original

    # Now perform LDL^T decomposition and solve
    print(f"\n=== ВЫПОЛНЯЕМ LDL^T РАЗЛОЖЕНИЕ И РЕШЕНИЕ СИСТЕМЫ ===")

    try:
        L, D = ldlt_decomposition(A_to_use)
        print("LDL^T разложение успешно выполнено")

        print(f"\nМатрица L:")
        print(L)

        print(f"\nМатрица D (диагональная):")
        print(D)

        print(f"\nМатрица L^T:")
        print(L.T)

        # Solve system and show x, y, z
        x, y, z = solve_ldlt(L, D, b)

        print(f"\n=== РЕШЕНИЕ СИСТЕМЫ ===")
        print(f"Вектор y (решение L y = b):")
        print(f"y = {y}")

        print(f"\nВектор z (решение D z = y):")
        print(f"z = {z}")

        print(f"\nВектор x (решение L^T x = z):")
        print(f"x = {x}")

        # Verify solution
        residual = np.linalg.norm(A_to_use.dot(x) - b)
        print(f"\nПроверка решения:")
        print(f"Норма невязки ||A x - b|| = {residual:.6g}")

    except ValueError as e:
        print(f"LDL^T разложение не удалось: {e}")
        # Fallback to numpy solve
        try:
            x = np.linalg.solve(A_to_use, b)
            print(f"\nРешение системы (через numpy.linalg.solve):")
            print(f"x = {x}")
            residual = np.linalg.norm(A_to_use.dot(x) - b)
            print(f"Норма невязки ||A x - b|| = {residual:.6g}")
        except np.linalg.LinAlgError as e:
            print(f"Решение системы невозможно: {e}")

    print("\n" + "=" * 60)
    print("ВЫЧИСЛЕНИЯ ЗАВЕРШЕНЫ")


if __name__ == "__main__":
    main()
