def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return f(x - 1, y) + f(x // 2, y)


print(f(int('100001', 2), int('100', 2)))
