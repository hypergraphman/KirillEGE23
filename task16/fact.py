def f(x):
    if x <= 1:
        return 1
    if x >= 2:
        return x * f(x - 1)


x = int(input())
k = 1
for i in range(1, x + 1):
    k = k * i
print(k)

print(f(5))