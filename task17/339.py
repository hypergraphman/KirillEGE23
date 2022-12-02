data = list(map(int, open("17-339.txt").readlines()))
k = 0
mx = -1 * 10 ** 10
data2 = filter(lambda x: x > 0 and x % 19 == 0, data)
mn = min(data2)
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if data[i - 1] + data[i] < mn:
        k += 1
        mx = max(mx, data[i - 1] + data[i])
print(mn)
print(k, abs(mx))
