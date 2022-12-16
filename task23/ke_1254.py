def f(x, dead=9):
    if dead == 0:
        return x
    s.add(f(x * 2, dead - 1))
    s.add(f(x * 2 + 1, dead - 1))


s = set()
f(1)
print(*s)
print(len(s))