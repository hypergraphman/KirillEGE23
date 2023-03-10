def f3(n):
    k = 0
    while n % 3 == 0:
        k += 1
        n //= 3
    return k


with open('27-B.txt') as f:
    n = int(f.readline())
    temp = list()
    for i in range(18):
        temp.append(int(f.readline()))
    b = [[0] * 8 for _ in range(8)]
    k = 0
    for _ in range(n - 18):
        x = temp.pop(0)
        y = int(f.readline())
        t = f3(x)
        if t > 7:
            t = 7
        b[x % 8][t] += 1
        k += sum(b[(8 - y % 8) % 8][-f3(y) - 1:])
        temp.append(y)
print(k)