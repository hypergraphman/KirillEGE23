k = 0
for x in range(200):
    for y in range(200):
        if (x / 106.52112466548595 < y / 61.5) and (x / 106.52112466548595 < (y - 123) / (61.5 - 123)) and x > 0:
            k += 1
print(k)


count = 0
for x in range(1, 200):
    for y in range(1, 200):
        if y < -x / 3 ** 0.5 + 123 and y > x / 3 ** 0.5:
            count += 1
print(count)
