import sympy
from sympy import diff
from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt

# 差分的对象
x = 16
k = 2  # 步长
x1 = x + k  # 向前
x2 = x - k  # 向后


# 方程式
def func(t):
    return 2000 * sympy.log(14 * 10000 / (14 * 10000 - 2100 * t)) - 9.8 * t


# 一阶向前差分
def for_difference():
    a_for_diff = (func(x1) - func(x)) / k
    for_error = abs(a_for_diff - a_true) / a_true
    print(f'{x}的一阶向前差分值：{a_for_diff}')
    print(f'{x}的一阶向前差分的误差：{for_error * 100}%')


# 一阶向后差分
def beh_difference():
    a_beh_diff = (func(x) - func(x2)) / k
    beh_error = abs(a_beh_diff - a_true) / a_true
    print(f'{x}的一阶向后差分值：{a_beh_diff}')
    print(f'{x}的一阶向后差分的误差：{beh_error * 100}%')


# 一阶中心差分
def cen_difference():
    a_cen_diff = (func(x1) - func(x2)) / (k * 2)
    cen_error = abs(a_cen_diff - a_true) / a_true
    print(f'{x}的二阶中心差分值：{a_cen_diff}')
    print(f'{x}的二阶中心差分的误差：{cen_error * 100}%')


# 二阶中心差分
def two_cen_difference():
    a_cen_diff = (func(x1) + func(x2) - 2 * func(x)) / (k ** 2)
    cen_error = abs(a_cen_diff - a_true) / a_true
    print(f'{x}的二阶中心差分值：{a_cen_diff}')
    print(f'{x}的二阶中心差分的误差：{cen_error * 100}%')


# 一阶向前差分
def for_difference(x1, x, a_true, k):
    a_for_diff = (func(x1) - func(x)) / k
    for_error = abs(a_for_diff - a_true) / a_true
    print(f'{x}的一阶向前差分值：{a_for_diff}')
    print(f'{x}的一阶向前差分的误差：{for_error * 100}%')
    return for_error


def Judge_precision(x):
    D = True
    k = 2  # 初始步长
    n = 0
    while D:
        n += 1
        x1 = x + k  # 向前
        t = symbols("t")
        a_true = diff(func(t), t).subs(t, x)
        error = for_difference(x1, x, a_true, k)
        if error <= 0.01:
            D = False
            print(f'迭代第{n}次后，{x}的一阶向前差分的误差为{error}')
        else:
            k = k / 2


# -----------------------------------------------------------------------

def difference_list(dlist):  # Newton
    if len(dlist) > 0:
        print(dlist)
        prev, curr = 0, 0
        n = []
        for i in dlist:
            curr = i
            n.append(curr - prev)
            prev = i
        n.pop(0)
        difference_list(n)


def difference_quotient_list(y_list, x_list=[]):
    if x_list == []:
        x_list = [i for i in range(len(y_list))]
    print(y_list)
    prev_list = y_list
    dq_list = []
    dq_list.append(prev_list[0])
    for t in range(1, len(y_list)):
        prev, curr = 0, 0
        m = []
        k = -1
        for i in prev_list:
            curr = i
            m.append((curr - prev) / (x_list[k + t] - x_list[k]))
            prev = i
            k += 1
        m.pop(0)
        prev_list = m
        dq_list.append(prev_list[0])
        print(m)
    return dq_list


def newton_interpolate(x_list, y_list, x):
    coef = difference_quotient_list(y_list, x_list)
    p = coef[0]
    for i in range(1, len(coef)):
        product = 1
        for j in range(i):
            product *= (x - x_list[j])
        p += coef[i] * product
    return p


if __name__ == '__main__':
    t = symbols("t")
    a_true = diff(func(t), t).subs(t, x)  # 真值
    for_difference()

    beh_difference()

    cen_difference()

    two_cen_difference()

    x = 16  # 差分对象
    # Judge_precision(x)

    x_points = [0, 1, 2, 3, 4, 5]
    y_points = [1, 5, 4, 8, 7, 12]
    # 牛顿插值
    x = np.linspace(0, 5)
    y = list(map(lambda t: newton_interpolate(x_points, y_points, t), x))
    # 画图
    plt.scatter(x_points, y_points, color="orange")
    plt.plot(x, y)
    plt.legend(["newton interpolation", "scattered points"])
    plt.show()
