f = open('26-99.txt')
n, m = map(int, f.readline().split())
a = [int(x) for x in f.readlines()]
a.sort()
trucks = []
# print(a)
while a:
    cur_sum = 0
    for i in range(len(a) - 1, -1, -1):
        if cur_sum + a[i] <= m:
            cur_sum += a.pop(i)
    trucks.append(cur_sum)
print(len(trucks), trucks[-2])
# print(trucks)
