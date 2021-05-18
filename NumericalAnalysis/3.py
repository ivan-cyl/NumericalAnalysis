import numpy as np
import sympy as sp

x = sp.Symbol("x")


def comTrapz(a, b, equal_segment, intergrand):
    """
    实现复合梯形求积公式
    :param a: 区间左端点即起点a
    :param b: 区间右端点即终点b
    :param equal_segment: 区间等分数n
    :param intergrand: 被积函数f(x)
    :return: 复合梯形求积积分
    """
    step_h = (b - a) / equal_segment
    f_x_k_array = np.array([intergrand.subs(x, a + k * step_h) for k in range(1, equal_segment)])
    return step_h / 2 * (intergrand.subs(x, a) + 2 * np.sum(f_x_k_array) + intergrand.subs(x, b))


def comSimpson(a, b, equal_segment, intergrand):
    """
    实现复合辛普森求积公式
    :param a: 区间左端点即起点a
    :param b: 区间右端点即终点b
    :param equal_segment: 区间等分数n
    :param intergrand: 被积函数f(x)
    :return: 复合辛普森求积积分
    """
    step_h = (b - a) / equal_segment
    f_x_k1_array = np.array([intergrand.subs(x, a + (k + 0.5) * step_h) for k in range(equal_segment)],
                            dtype=np.float64)
    f_x_k2_array = np.array([intergrand.subs(x, a + k * step_h) for k in range(1, equal_segment)],
                            dtype=np.float64)
    return step_h / 6 * (
            intergrand.subs(x, a) + 4 * np.sum(f_x_k1_array) + 2 * np.sum(f_x_k2_array) + intergrand.subs(x, b))


if __name__ == '__main__':
    fx = 4 / (1 + x ** 2)
    print("复合梯形求积公式计算结果为：")
    print(comTrapz(0, 1, 4, fx))
    print("复合辛普森求积公式计算结果为：")
    print(comSimpson(0, 1, 4, fx))
