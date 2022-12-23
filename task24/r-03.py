line = open("k8.txt").readline()
template = 'EAB'
cur_len = 0
max_len = 0
for c in line:
    if c == template[cur_len % len(template)]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    elif c == template[0]:
        cur_len = 1
    else:
        cur_len = 0
print(max_len)