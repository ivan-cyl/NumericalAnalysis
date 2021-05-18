import sympy as sp

x = sp.Symbol("x")
point = 1


# point代表有多少个零点的多项式
def P():
    if point == 0:
        return 1
    elif point == 1:
        return x
    p0 = 1
    p1 = x
    for i in range(point - 1):
        temp = ((2 * i + 3) * x * p1 - (i + 1) * p0) / (i + 2)
        p0 = p1
        p1 = temp
    return p1
