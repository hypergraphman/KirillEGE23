def f(x, y, p):
    if p == 2  or p == 4:
        if x + y >= 77:
            return True
        if p == 4:
            return False
    if x + y >= 77:
        return False
    if p % 2 != 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)


for s in range(1, 70):
    if f(7, s, 0):
        print(s)
