import numpy as np


def difference_quotient_coefficient(x_array: np.ndarray, y_array: np.ndarray):
    """
    实现牛顿均差插值多项式各阶均差系数
    :param x_array: 横坐标数组
    :param y_array: 纵坐标数组
    :return: 各阶均差系数数组
    """
    nth = x_array.shape[0]
    # 初始化均差系数数组
    difference_quotient_array = np.zeros(nth)
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


def newtown_base_function(symbol_x, x_array: np.ndarray):
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
