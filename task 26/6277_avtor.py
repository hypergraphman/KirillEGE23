n, v, *a = map(int, open('26_6277.txt').read().split())
f = 0
c = []
for d in a:
    while sum(c) + d > v:
        if f == 0:
            f = v - sum(c)
        c.remove(max((x for x in c if x <= d)))
    c.append(d)
print(f, len(c))