from re import fullmatch

# for i in range(2023, 2 * 10**9, 2023):
#     if fullmatch(r'1\d2139\d*4', str(i)):
#         print(i, i // 2023)
# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048

for x in range(10):
    for z in [''], range(0, 1000):
        for y in z:
            t = int(f'1{x}2139{y}4')
            if t % 2023 == 0:
                print(t, t // 2023)