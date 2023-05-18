f = open("27-151b.txt")
n = int(f.readline())
k = int(f.readline())
step = []

ostat100_del37 = [0] * 100
ostat100_notdel37 = [0] * 100

for _ in range(k):
    step.append(int(f.readline()))

cnt = 0
for i in range(n - k):
    num = int(f.readline())
    if step[i % k] % 37 == 0:
        ostat100_del37[step[i % k] % 100] += 1
    else:
        ostat100_notdel37[step[i % k] % 100] += 1
    if num % 37 == 0:
        cnt += ostat100_notdel37[num % 100]
    else:
        cnt += ostat100_del37[num % 100]
    step[i % k] = num

print(cnt)
