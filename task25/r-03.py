def delit(n):
    r = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2:
                r.add(i)
            if n // i % 2:
                r.add(n // i)
    return r


a = 77777777
b = 88888888
for x in range(a, b + 1):
    t = delit(x)
    if len(t) == 5:
        print(x, sorted(t)[1])
