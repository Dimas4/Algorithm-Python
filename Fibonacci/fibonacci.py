from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)


@lru_cache(maxsize=None)
def fib(n):
    result = []
    i, x, y = 0, 0, 1
    while i < n:
        result.append(y)
        x, y, i = y, x + y, i + 1
    return result
