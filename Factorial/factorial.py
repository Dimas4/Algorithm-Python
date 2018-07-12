from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(n):
    return 1 if n <= 1 else factorial(n-1) * n


@lru_cache(maxsize=None)
def factorial_while(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1
    return result


def factorial_array(n):
    array = [0 for _ in range(n+1)]
    array[0] = 1
    for i in range(1, n+1):
        array[i] = array[i-1] * i
    return array[-1]

