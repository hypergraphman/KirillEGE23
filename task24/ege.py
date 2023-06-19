s = open('24gen.txt').read()
a = [len(x) for x in s.split('T')][1:-1]
min_s = 10**10
for i in range(len(a)-210):
    min_s = min(min_s, sum(a[i:i + 209]) + 210)
print(min_s)

i_t = []
for i in range(len(s)):
    if s[i] == 'T':
        i_t.append(i)
min_L = 10**20
for i in range(210, len(i_t)):
    min_L = min(min_L, i_t[i] - i_t[i - 209])
print(min_L+1)