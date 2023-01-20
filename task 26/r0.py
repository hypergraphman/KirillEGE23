for j in range(1, 20):
    f = open(f'26-{j}.txt')
    v, n = map(int, f.readline().split())
    a = sorted(map(int, f.readlines()))
    i = 0
    while i < n and v - a[i] >= 0:
        v -= a[i]
        i += 1
    print(i, end=' ')
    v += a[i - 1]
    while i < n and v - a[i] >= 0:
        i += 1
    print(a[i - 1])
    f.close()