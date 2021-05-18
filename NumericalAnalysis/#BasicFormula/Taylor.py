import sympy as sp
import numpy as np


def taylor(func, num_terms=3, point=0):
    # 默认泰勒展开3项，在x0=0出展开
    sums = 0
    for i in range(num_terms):
        numerator = func.diff(x, i)
        numerator = numerator.evalf(subs={x: point})
        denominator = np.math.factorial(i)
        # 取得i的阶乘
        sums += numerator / denominator * (x - point) ** i
        # 泰勒展开式表达式子
    return sp.simplify(sums)


x = sp.Symbol('x')
