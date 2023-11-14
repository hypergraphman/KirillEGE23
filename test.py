from math import sqrt


class MyExcept(Exception):
    pass


def vich(x):
    p1 = 1
    k1 = 1
    p2 = 2
    k2 = 4
    t = 1
    st_x = x
    cur = x / 2
    s = 1 + cur
    st_ = -1
    while abs(cur) > 0.000001:
    # for _ in range(10):
        p1 *= k1
        p2 *= k2
        st_x *= x
        pre_cur = cur
        cur = st_ * p1 * st_x / p2
        if abs(pre_cur) < abs(cur):
            raise MyExcept
        # print(p1, p2, p1 * st_x / p2, cur)
        s += cur
        k1 += 2
        k2 += 2
        st_ *= -1
        t += 1
    return s
def math(x):
    return sqrt(x + 1)


values = [-0.84, 1, 2]  # для двойки не работает
for x in values:
    try:
        print("x = ", x, ", S(x) = ", vich(x), ", f(x) = ", math(x))
    except MyExcept:
        print('программа упала. числитель стал больше знаменателя по модулю.')

