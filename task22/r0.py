d = dict()
for line in open('22-6.txt').readlines():
    t = line.split('\t')
    id = int(t[0])
    if t[2][0] == '0':
        d[id] = int(t[1])
    elif t[2][0] != '"':
        d[id] = int(t[1]) + d[int(t[2])]
    else:
        mx = 0
        for x in list(map(int, t[2][1:-2].split(';'))):
            if d[x] > mx:
                mx = d[x]
        d[id] = int(t[1]) + mx
print(max(d.values()))