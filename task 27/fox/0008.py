f = open('27_b.txt')
n = int(f.readline())
a = []
k = 30
for line in f.readlines():
    km, kg = map(int, line.split())
    a.append((km, (kg + k - 1) // k))
for i in range(550010, 550210):
    s = 0
    for j in range(n):
        s += a[j][1] * abs(a[i][0] - a[j][0])
    print(i, s)
# A 62393
# B 7879886864050