def f3(n):
    k = 0
    while n % 3 == 0:
        k += 1
        n //= 3
    return k


with open('27-A.txt') as f:
    n = int(f.readline())
    temp = list()
    for i in range(18):
        temp.append(int(f.readline()))
    b = [0] * 8
    k = 0
    for _ in range(n - 18):
        x = temp.pop(0)
        y = int(f.readline())
        b[f3(x)] += 1
        k += sum(b[-f3(y) - 1:])
        # k += b[(8 - y % 8) % 8]
        temp.append(y)
    # for _ in range(n - 18):
    #     x = temp.pop(0)
    #     y = int(f.readline())
    #     b[x % 8] += 1
    #     k += b[(8 - y % 8) % 8]
    #     temp.append(y)
print(k)

# 2589