import sympy as sp
import numpy as np


def taylor(func, num_terms=3, point=0):
    # 默认泰勒展开3项，在x0=0出展开
    sums = 0
    for i in range(num_terms):
        numerator = func.diff(x, i)
        # 使用diff求差值，后一项减前一项
        numerator = numerator.evalf(subs={x: point})
        denominator = np.math.factorial(i)
        # 取得i的阶乘
        sums += numerator / denominator * (x - point) ** i
        # 泰勒展开式表达式子
    return sp.simplify(sums)


x = sp.Symbol('x')
exp = sp.log(x)
# 默认为e为底
i = 1
real = np.log(3)
error = 10000
while error > 1e-3:
    exp_tay = taylor(exp, num_terms=i, point=np.exp(1))
    print('展开到', i - 1, '项，表达式为')
    sp.pprint(exp_tay)
    result = exp_tay.evalf(subs={x: 3})
    error = np.abs(result - real)
    i += 1
    print('第', i - 1, '项误差为', error)

import numpy
import sympy as sp


def shao_expand(func, num_terms=3, point=0):
    sums = []
    for i in range(num_terms):
        numerator = func.diff(x, i)
        numerator = numerator.evalf(subs={x: point})
        denominator = np.math.factorial(i)
        sums.append(numerator / denominator)
    return sums


def shao_cal(in_x, sums, point):
    lenth = len(sums)
    result = sums[lenth - 1]
    result = np.around(result, decimals=3)
    for i in range(1, lenth):
        result = result * (in_x - point) + sums[lenth - i - 1]
        result = np.around(result, decimals=3)
    return result


x = sp.Symbol('x')
px = (x) ** 4 + 0.2 * (x) ** 3 + 0.05 * (x) ** 2 - 0.005 * (x) + 0.001
coef = shao_expand(px, num_terms=5, point=0)
coef = np.array(coef, dtype='float32')
print('泰勒展开从高到低的系数依次为', coef)
print('秦九韶，保留三位算出值：', shao_cal(in_x=0.11, sums=coef, point=0))
print('高精度计算结果', px.evalf(subs={x: 0.11}))


def cp(in_x, func):
    df = func.diff(x, 1)
    df = df.evalf(subs={x: in_x})
    f = func.evalf(subs={x: in_x})
    return np.abs(df * in_x / f)


print('条件数为', cp(0.11, px))
