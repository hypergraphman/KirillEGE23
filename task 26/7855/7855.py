f = open("26_7855.txt")
k = int(f.readline())
n = int(f.readline())

mx = 0
book = [float('inf')] + [0] * k
i_k = 0
data = []
for _ in range(n):
    p, out = map(int, f.readline().split())
    data.append((p, out))
data.sort()

t = 0
for p, out in data:
    i_k = 0
    for i in range(1, len(book)):
        if book[i] <= book[i_k]:
            i_k = i
    if book[i_k] - p > 0 and book[i_k] - p > mx:
        mx = book[i_k] - p
    book[i_k] = out + 31
    if book[i_k] <= 7 * 24 * 60:
        t = i_k
print(mx, t)
