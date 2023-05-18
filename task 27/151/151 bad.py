f = open("27-151a.txt")
n = int(f.readline())
k = int(f.readline())
a = []

for _ in range(n):
    a.append(int(f.readline()))

cnt = 0
for i in range(n):
    for j in range(i + 1, min(k + i + 1, n)):
        if (a[i] - a[j]) % 100 == 0 and ((a[i] % 37 == 0) != (a[j] % 37 == 0)):
            cnt += 1
            # print(i, j)
print(cnt)
