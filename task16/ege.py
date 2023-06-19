from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 11:
        return 10
    return n + f(n - 1) * n


for i in range(1, 2024):
    f(i)

print((f(2024) - f(2022)) % 131)