l = open("k8.txt").readline()
s1 = "BCD"
s2 = "BDE"
s3 = "BCE"
k = 0
for i in range(0, len(l) - 2):
    if (l[i] in s1 and
       l[i + 1] in s2 and l[i] != l[i + 1] and
       l[i + 2] in s3 and l[i + 1] != l[i + 2]):
        k += 1
        print(l[i:i + 3])

print(k)
