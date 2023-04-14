f = open('27-142a.txt')
p = 20
n, k, m = map(int, f.readline().split())
a = [0] * (k)
for i in range(n):
    home, letter = map(int, f.readline().split())
    a[home % k] = (letter + p - 1) // p

min_s = 10**10
ans = None

for x in range(1, k):
    f = True
    for i in range(x - m + 1, x + m):
        if a[i % k]:
            f = False
            break
    s = 0
    for i in range(1, k // 2 + k % 2):
        s += a[(x - i) % k] * i
    for i in range(1, k // 2 + 1):
        s += a[(x + i) % k] * i
    if f:
        if s < min_s:
            min_s = s
            ans = x
print(ans, min_s)