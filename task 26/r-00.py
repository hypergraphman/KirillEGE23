f = open("26.txt").readlines()
n = 8200
f = f[1::]
sum_p = 0
m = 0
s = 0
count=0
kn = 0
f.sort()
for i in range(0, len(f)):
    if n >= sum_p + int(f[i]):
        kn+=1
        sum_p += int(f[i])
    num = int(f[i - 1])
    k = n - sum_p
    s = num + k
for x in range(0, s + 1):
    if x in f:
        count = x
print(kn,count)
