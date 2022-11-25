for x in range(15):
    num1 = 15**4 + 2 * 15**3 + 3 * 15**2 + x * 15 + 5
    num2 = 15**4 + x * 15**3 + 2 * 15**2 + 3 * 15 + 3
    if (num1 + num2) % 14 == 0:
        print((num1 + num2) // 14)