def find_the_multiplication(a, b, c):
    return a * b * c

def find_the_factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * find_the_factorial(a - 1)