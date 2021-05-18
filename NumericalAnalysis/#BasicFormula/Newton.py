import numpy as np
from sympy import expand


def difference_quotient_coefficient(x_array, y_array):
    """
    实现牛顿均差插值多项式各阶均差系数
    :param x_array: 横坐标数组
    :param y_array: 纵坐标数组
    :return: 各阶均差系数数组
    """
    nth = x_array.shape[0]
    # 初始化均差系数数组
    difference_quotient_array = np.zeros(nth)
    # 产生返回0数组
    difference_quotient_array[0] = y_array[0]
    # 求各阶均差
    for i in range(1, nth):
        nth_difference_quotient = np.zeros(nth - i)
        # 求每阶均差
        for j in range(nth - i):
            nth_difference_quotient[j] = (y_array[j + 1] - y_array[j]) / (x_array[i + j] - x_array[j])
        difference_quotient_array[i] = nth_difference_quotient[0]
        y_array = nth_difference_quotient
    return difference_quotient_array


def newtown_base_function(symbol_x, x_array):
    """
    实现牛顿均差插值基函数
    :param symbol_x: 符号变量x
    :param x_array: 横坐标数组
    :return: 牛顿均差插值基函数数组
    """
    nth = x_array.shape[0]
    base_function_array = np.zeros(nth, dtype=np.ndarray)
    # base_function_array = list(np.zeros(nth))
    base_function_array[0] = 1
    for i in range(1, nth):
        base_function_array[i] = np.prod(symbol_x - x_array[:i], dtype=np.ndarray)
    return base_function_array


def newtown(x_array, y_array, symbol_x):
    """
    实现牛顿均差插值多项式
    :param x_array: 插值结点横坐标数组
    :param y_array: 插值结点纵坐标数组
    :param symbol_x: 符号变量x
    :return: 牛顿均差插值多项式
    """
    return expand(np.sum(difference_quotient_coefficient(x_array, y_array) * newtown_base_function(symbol_x, x_array)))


def qin_jiu_shao(coefficient_array: np.ndarray, value, is_ascending_order: bool = False):
    """
    多项式求值的秦九韶算法,即Horner算法
    :param coefficient_array: 多项式系数数组
    :param value: 自变量的值
    :param is_ascending_order: 多项式排列顺序
    :return: the value of polynomial
    example:
    2*x**4 - 3*x**2 + 3*x - 4=((((2x+0)x-3)x+3)x-4)
    3*x**5 - 2*x**3 + x + 7=(((((3x+0)x-2)x+0)x+1)x+7)
    """
    if is_ascending_order:
        coefficient_array = coefficient_array[::-1]
    degree = coefficient_array.shape[0]
    b = coefficient_array[0]
    for i in range(1, degree):
        b = b * value + coefficient_array[i]
    return b


# -----------------------------------------------------------

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
    import numpy as np
    import matplotlib.pyplot as plt

    # 待插值的元素值
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
