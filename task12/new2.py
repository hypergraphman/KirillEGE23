for x in range(100):
    for y in range(100):
        for z in range(100):
            for w in range(100):
                if y + 2 * w == 47 and 2 * z + x == 68 and 2 * x + z == 2 * y + w:
                    print(x, y, z, w)