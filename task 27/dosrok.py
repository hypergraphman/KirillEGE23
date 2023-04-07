f = open("27-B.txt")
k = int(f.readline())
n = int(f.readline())

data = []
for _ in range(k):
    data.append(int(f.readline()))

mx_left, mx = 0, 0
for i in range(n - k):
    x = int(f.readline())
    mx_left = max(mx_left, data[i % k])
    mx = max(mx, mx_left + x)
    data[i % k] = x
print(mx)

