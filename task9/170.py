c = 0
for line in open('9-170.txt').readlines():
    m = list(map(int, line.split()))
    m_s = set(m)
    if len(m_s) == 5:
        f = sum(m) - sum(m_s)
        if (sum(m_s) - f) / 4 <= f * 2:
            c += 1
print(c)
