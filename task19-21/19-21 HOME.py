def f(x, p):
    if p == 2 :
        if x == 42:
            return True
        else:
            return False
    if x == 42:
        return False
    if x > 42:
        if p % 2 != 0:
            return f(x - 1, p + 1) or f(x - 3, p + 1) or f(x - 7, p + 1)
        if p % 2 == 0:
            return f(x - 1, p + 1) and f(x - 3, p + 1) and f(x - 7, p + 1)
    if x < 42:
        if p % 2 != 0:
            return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x + 7, p + 1)
        if p % 2 == 0:
            return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x + 7, p + 1)


for s in range(0, 100):
    if f(s, 0):
        print(s)

#20 31 37
#21 50