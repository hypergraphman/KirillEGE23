from re import fullmatch
from functools import reduce

mx = ''
for num in open("k8.txt").readline().replace('KKK', 'KKKK').split('KK'):
    if fullmatch(r'43\d\d78\d\d\d34', num):
        if num > mx:
            mx = num
print(reduce(lambda x, y: x * y, map(int, filter(lambda x: x in '13579', mx))))
