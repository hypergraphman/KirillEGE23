from functools import cache

x = int(input())
k1 = k2 = 1
for _ in range(x - 2):
    k1, k2 = k2, k1 + k2
print(k2)


@cache
def f(x):
    if x <= 2:
        return 1
    if x > 2:
        return f(x - 1) + f(x - 2)


for i in range(1, 1000):
    f(400 * i)

print(f(x))