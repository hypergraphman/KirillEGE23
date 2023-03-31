def f(a, c, m):
    if a == 42:
        return c % 2 == m % 2
    if c == m:
        return False
    if a > 42:
        moves = [f(a - 1, c + 1, m), f(a - 3, c + 1, m), f(a - 7, c + 1, m)]
    else:
        moves = [f(a + 1, c + 1, m), f(a + 3, c + 1, m), f(a + 7, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for a in range(41, 42 - 30, -1):
    for m in range(0, 5):
        if f(a, 0, m):
            print(a, m)
            break

for a in range(43, 43 + 30):
    for m in range(0, 5):
        if f(a, 0, m):
            print(a, m)
            break

#19 28
#20 31, 37
#21 50