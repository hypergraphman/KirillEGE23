from string import digits, ascii_uppercase


def n_to_p(n, p):
    s = ''
    alf = digits + ascii_uppercase
    while n > 0:
        s = alf[n % p] + s
        n //= p
    return s


x = 49 ** 7 + 7 ** 21 - 7
print(n_to_p(x, 7).count("6"))
