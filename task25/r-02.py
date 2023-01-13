def delit(n):
    r = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)

# print(delit(60))
a = 174457
b = 174505
for n in range(a, b + 1):
    t = delit(n)
    if len(t) == 4:
        print(*t[1:3])


# 3 58153 174459
# 7 24923 174461
# 59 2957 174463
# 13 13421 174473
# 149 1171 174479
# 5 34897 174485
# 211 827 174497
# 2 87251 174502