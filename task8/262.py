from itertools import product

alf = '01234567'
p = [el + '6' for el in '1357'] + ['6' + el for el in '1357']
c = 0
for word in product(alf, repeat=5):
    word = ''.join(word)
    if word.count('6') == 1 and all([x not in word for x in p]) and word[0] != '0':
        c += 1
print(c)
