from string import ascii_uppercase, digits

d = digits + ascii_uppercase

*data, = map(lambda x: x.strip(), open('17-362.txt').readlines())

res = []

for p1, p2 in zip(data, data[1:]):
    if abs(d.find(max(p1)) - d.find(max(p2))) <= 2:
        res.append(int(p1, d.find(max(p1)) + 1) + int(p2, d.find(max(p2)) + 1))
print(len(res), max(res))