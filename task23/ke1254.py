from itertools import product

mul2 = lambda x: x * 2
mul2_plus1 = lambda x: x * 2 + 1

s = set()
for ops in product((mul2, mul2_plus1), repeat=9):
    t = ops[0](1)
    for i in range(1, len(ops)):
        t = ops[i](t)
    s.add(t)
print(len(s))