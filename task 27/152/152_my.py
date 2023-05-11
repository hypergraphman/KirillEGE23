from collections import defaultdict


def extract(n):
    n2 = n5 = 0
    while n % 2 == 0:
        n2 += 1
        n //= 2
    while n % 5 == 0:
        n5 += 1
        n //= 5
    return n2, n5


n, *a = map(int, open('27-152d.txt'))

d = 5
# counter = defaultdict(int)
counter = [[0] * 7 for _ in range(7)]
k = 0
for el in a:
    n2, n5 = extract(el)
    if n2 > 5:
        n2 = 6
    if n5 > 5:
        n5 = 6
    # for n2a, n5a in counter:
    #     if min(n2 + n2a, n5 + n5a) == d:
    #         k += counter[(n2a, n5a)]
    # k += sum(counter[(n2a, n5a)] for n2a, n5a in counter if min(n2 + n2a, n5 + n5a) == d)
    # counter[(n2, n5)] += 1
    counter[n2][n5] += 1

for n2 in range(7):
    for n5 in range(7):
        amount = 0
        for n2a in range(7):
            for n5a in range(7):
                if min(n2 + n2a, n5 + n5a) == d:
                    amount += counter[n2a][n5a]
        k += counter[n2][n5] * amount

# print(k)
print(k // 2)
