from functools import lru_cache


@lru_cache(None)
def delit(n):
    r = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


i = 100000
k = 5
while k != 0:
    n = int(str(i) + str(i)[-2::-1])
    if all(int(x) % 2 == 0 for x in str(i)[1::2]) and all(int(x) % 2 != 0 for x in str(i)[::2]) and delit(n)[-2] % 7 == 0:
        print(n, delit(n)[-2])
        k -= 1
    i += 1