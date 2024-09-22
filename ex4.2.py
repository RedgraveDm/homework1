import itertools


def cycle_factorial(n):
    return list(itertools.accumulate(range(1, n + 2), lambda a, b: a * min(b, max(1, b - 1))))


print(cycle_factorial(int(input())))
