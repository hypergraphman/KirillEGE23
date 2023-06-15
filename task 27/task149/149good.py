f = open("27-149a.txt")
n = int(f.readline())
k = int(f.readline())

del47_2023 = [0] * 2023
notdel47_2023 = [0] * 2023

mx = 0
for i in range(k + 1):
    el = int(f.readline())
    if el % 47 == 0:
        mx = max(notdel47_2023[(2023 - el % 2023) % 2023] + el, mx)
        del47_2023[el % 2023] = max(del47_2023[el % 2023], el)
    else:
        mx = max(del47_2023[(2023 - el % 2023) % 2023] + el, mx)
        notdel47_2023[el % 2023] = max(notdel47_2023[el % 2023], el)

for i in range(k + 1, n):
    el = int(f.readline())
    if el % 47 == 0:
        del47_2023[el % 2023] -= 1
    else:
        notdel47_2023[el % 2023] -= 1

    if el % 47 == 0:
        mx = max(notdel47_2023[(2023 - el % 2023) % 2023] + el, mx)
        del47_2023[el % 2023] = max(del47_2023[el % 2023], el)
    else:
        mx = max(del47_2023[(2023 - el % 2023) % 2023] + el, mx)
        notdel47_2023[el % 2023] = max(notdel47_2023[el % 2023], el)

print(mx)
