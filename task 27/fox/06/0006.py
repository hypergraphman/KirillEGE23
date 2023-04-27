f = open("27_B.txt")
n = int(f.readline())
a = []
k = 81
for _ in range(n):
    km, puck = map(int, f.readline().split())
    a.append((km, (puck + k - 1) // k))
for i in range(989800, 989820):
    s = 0
    for j in range(n):
        s += a[j][1] * abs(a[i][0] - a[j][0])
    print(i, s)
#161148 A

