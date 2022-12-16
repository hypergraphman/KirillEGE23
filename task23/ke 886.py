def f(x, y, k):
    if x == y:
        if k == 7:
            return 1
        else:
            return 0
    if x > y:
        return 0
    return f(x + 1, y, k + 1) + f(x + 4, y, k + 1) + f(x * 2, y, k + 1)


print(f(3, 27, 0))
