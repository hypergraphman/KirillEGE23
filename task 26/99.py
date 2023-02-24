f = open('26-99.txt')
n, m = map(int, f.readline().split())
a = [int(x) for x in f.readlines()]
a.sort(reverse=True)
trucks = []
# print(a)
while a:
    cur_sum = 0
    i = 0
    while i < len(a):
        if cur_sum + a[i] <= m:
            cur_sum += a.pop(i)
        else:
            i += 1
    trucks.append(cur_sum)
print(len(trucks), trucks[-2])
# print(trucks)
