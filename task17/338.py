data = list(map(int, open('17-338.txt').readlines()))
mn = min(data)
k = 0
mx = -1 * 10**10
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if p1 % 117 == mn or p2 % 117 == mn:
        k += 1
        mx = max(mx, p1 + p2)
print(k, mx)