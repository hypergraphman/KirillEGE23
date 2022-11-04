for k in range(200, 101, - 1):
    for m in range(200, 101, -1):
        for n in range(100, 201):
            s = "1" * k + "2" * m + "0" * n
            if sum(map(int, s)) == 599:
                pass
    print(k)
