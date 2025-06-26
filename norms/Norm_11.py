def add(a, b, *args, **kwargs):
    return sum((a, b) + args + tuple(kwargs.values()))

def is_odd(num):
    return num % 2 != 0

