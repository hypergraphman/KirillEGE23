with open('26-103.txt') as f:
    n, k, m = map(int, f.readline().split())
    a = []
    for line in f.readlines():
        r, c = line.split()
        a.append((int(r), c))
a.sort()
b = []
while a:
    c = [a.pop()]
    i = len(a) - 1
    while i >= 0 and len(c) < m:
        if abs(c[-1][0] - a[i][0]) >= k and c[-1][1] != a[i][1]:
            c.append(a.pop(i))
        i -= 1
    b.append(len(c))
print(len(b), b.count(m))
