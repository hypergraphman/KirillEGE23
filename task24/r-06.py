l = open("k8.txt").readline()
mx = 0
k = 1
for i in range(0, len(l) - 1):
    if l[i] == l[i + 1]:
        k += 1
        mx = max(mx, k)
    else:
        k = 1
print(mx)