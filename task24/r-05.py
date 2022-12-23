l = open("k8.txt").readline()
k = 1
mx = 0
s = ""
for i in range(0, len(l) - 1):
    if l[i] == l[i + 1]:
        k += 1
        if k > mx:
            mx = k
            s = l[i]
    else:
        k = 1
print(s, mx)
