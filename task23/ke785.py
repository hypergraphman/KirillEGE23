def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x + x + 1 + x % 2, y)


print(f(3, 25) * f(25, 75))
