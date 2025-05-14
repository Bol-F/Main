import numpy as np
import matplotlib.pyplot as plt

# Define the original piecewise function on [-2, 2]
def f(x):
    # Periodic extension of period 4
    x_mod = ((x + 2) % 4) - 2
    return np.where((x_mod >= 0) & (x_mod < 2), 3, 0)

# Partial sums definitions
def S_n(x, N):
    """Partial Fourier sum up to N (odd terms only)"""
    s = 3  # a0 term
    for n in range(1, N+1):
        if n % 2 == 1:  # only odd n have nonzero b_n
            b_n = 6 / (n * np.pi)
            s += b_n * np.sin(n * np.pi * x / 2)
    return s

# Define S1, S2, S3 explicitly
def S1(x):
    return S_n(x, 1)

def S2(x):
    # S2 same as S1 since b2=0
    return S_n(x, 2)

def S3(x):
    return S_n(x, 3)

# High N approximation to represent "Fourier function"
def S_high(x, N=50):
    return S_n(x, N)

# Plot over one period [-2, 2]
x_vals = np.linspace(-2, 2, 1000)
plt.figure(figsize=(12, 6))
plt.plot(x_vals, f(x_vals), label='Original f(x)', linewidth=2)
plt.plot(x_vals, S1(x_vals), label='S1(x)')
plt.plot(x_vals, S2(x_vals), label='S2(x)')
plt.plot(x_vals, S3(x_vals), label='S3(x)')
plt.plot(x_vals, S_high(x_vals), label='Fourier approx (N=50)', linestyle='--')
plt.title('Original Function, Partial Sums S1, S2, S3, and High‑N Fourier Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.ylim(-0.5, 3.5)
plt.show()
