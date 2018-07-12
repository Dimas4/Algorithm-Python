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


def fib_array(n):
    array = [0 for _ in range(n+1)]
    array[:2] = 0, 1
    for i in range(2, n+1):
        array[i] = array[i-1] + array[i-2]
    return array[-1]
