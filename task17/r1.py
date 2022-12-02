k = 0
mx = 0
a = (7, 17, 19, 27)
for n in range(1017, 7937 + 1, 3):
    if all(map(lambda x: n % x, a)):
        k += 1
        mx = n
print(k, mx)