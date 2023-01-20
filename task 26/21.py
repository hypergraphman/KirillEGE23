f = open('26-k1.txt')
n, k = map(int, f.readline().split())
a = sorted(map(int, f.readlines()))[::-1]
print(a[k])
print(int(sum(a[:k]) * 0.2))
