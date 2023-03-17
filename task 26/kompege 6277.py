n, v, *s = map(int, open("26_6277.txt").read().split())
cash = []
s = s[::-1]
while v - s[-1] >= 0:
    cash.append(s[-1])
    v -= s[-1]
    s.pop()
print(v)
while s:
    if v >= s[-1]:
        v -= s[-1]
        cash.append(s.pop())
    else:
        t = min(filter(lambda x: x >= s[-1] - v, cash), default=-1)
        if t > 0:
            cash.remove(t)
            v += t
            cash.append(s[-1])
            v -= s.pop()
        else:
            x = max(cash)
            v += x
            cash.remove(x)
print(len(cash))
