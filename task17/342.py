data = list(map(int, open("17-342.txt").readlines()))
k = 0
mn = 10 ** 10
min_37 = filter(lambda x: x % 37 == 0, data)
max_73 = filter(lambda x: x % 73 == 0, data)
mn_37 = min(min_37)
mx_73 = max(max_73)
mx_ = max(mn_37, mx_73)
mn_ = min(mn_37, mx_73)
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if (mn_ < p1 < mx_) != (mn_ < p2 < mx_):
        k += 1
        mn = min(mn, p1 + p2)

print(k, mn)
