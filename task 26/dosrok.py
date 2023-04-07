f = open("26.txt")

k = int(f.readline())
n = int(f.readline())
a = []
for i in range(n):
    a.append(tuple(map(int, f.readline().split())))
a.sort()
box = [0] * (k + 1)
c = 0
last = 0
for s, e in a:
    for i in range(1, len(box)):
        if box[i] < s:
            box[i] = e
            c += 1
            last = i
            break
print(c, last)