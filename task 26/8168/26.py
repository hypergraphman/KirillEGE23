f = open('26_8168.txt')
k = int(f.readline())
n = int(f.readline())
amount_p = 0
all_time_limit = 0
bags = [(0, 0)] * (k + 1)
a = []
for i in range(n):
    t1, t2 = map(int, f.readline().split())
    a.append((t1, t1 + t2))
a.sort()
for i in range(len(a)):
    t1, t2 = a[i]
    for j in range(1, len(bags)):
        if bags[j][1] < t1:
            bags[j] = (t1 + 1, t2)
            mn = float('inf')
            mx = 0
            for x in range(1, len(bags)):
                if bags[x][1] < mn:
                    mn = bags[x][1]
                if bags[x][0] > mx:
                    mx = bags[x][0]
            all_time_limit += max(0, mn - mx)
            break
    else:
        amount_p += 1
print(amount_p, all_time_limit)