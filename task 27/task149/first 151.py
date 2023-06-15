f = open("27-149b.txt")
n = int(f.readline())
k = int(f.readline())
step = []

d = 47

ostat2023_del47 = [0] * 2023
ostat2023_notdel47 = [0] * 2023

for _ in range(k):
    step.append(int(f.readline()))

mx = 0
for i in range(n - k):
    num = int(f.readline())
    if step[i % k] % d == 0:
        ostat2023_del47[step[i % k] % 2023] = max(step[i % k],  ostat2023_del47[step[i % k] % 2023])
    else:
        ostat2023_notdel47[step[i % k] % 2023] = max(step[i % k],  ostat2023_notdel47[step[i % k] % 2023])
    if num % d == 0:
        if ostat2023_notdel47[(2023 - num % 2023) % 2023]:
            mx = max(ostat2023_notdel47[(2023 - num % 2023) % 2023] + num, mx)
    else:
        if ostat2023_del47[(2023 - num % 2023) % 2023]:
            mx = max(ostat2023_del47[(2023 - num % 2023) % 2023] + num, mx)
    step[i % k] = num

print(mx)
