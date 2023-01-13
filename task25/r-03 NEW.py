def delit(n):
    r = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


a = 77777777
b = 88888888
arr = []
for x in range(0, 27):
    for p in range(3, 98):
        t = 2 ** x * p ** 4
        if len(delit(p)) == 2 and  a <= t <= b:
            #print(t, p)
            arr.append((t, p))
arr.sort()
print(*arr, sep='\n')
