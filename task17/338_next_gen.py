from itertools import pairwise

data = list(map(int, open('17-338.txt').readlines()))
# print(data)
mn = min(data)
# mn = 10**10
# for i in data:
#     if i < mn:
#         mn = i
# mn = min(filter(lambda x: x % 12 == 0, data))
# mn = 10**10
# for i in data:
#     if i % 12 == 0 and i < mn:
#         mn = i
data2 = list(filter(lambda x:  x[0] % 117 == mn or x[1] % 117 == mn, pairwise(data)))
p = max(data2, key=lambda x: x[0] + x[1])
print(len(data2), p[0] + p[1])