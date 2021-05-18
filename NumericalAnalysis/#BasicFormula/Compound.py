import numpy as np


# 复合梯形公式
def Compound_trapezoid(x, h, f):
    result = 0.0
    n = len(x) - 1
    for k in range(n):
        result += f(x[k]) + f(x[k + 1])
    result *= h / 2
    return result


# 复合辛普森公式
def Compound_Simpson(x, h, f):
    result = 0.0
    n = len(x) - 1
    for k in range(n):
        result += f(x[k]) + 4 * f(x[k] + h / 2) + f(x[k + 1])
    result *= h / 6
    return result


# ------------------------------------------------------------------------------------


def com_trapz(a, b, equal_segment, intergrand):
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


def com_simpson(a, b, equal_segment, intergrand):
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


Xk = [
    [0.0000000],
    [-0.5773503, 0.5773503],
    [-0.7745967, 0.0000000, 0.7745967],
    [-0.8611363, -0.3399810, 0.3399810, 0.8611363],
    [-0.9061798, -0.5384693, 0.0000000, 0.5384693, 0.9061798],
    [-0.9324695, -0.6612094, -0.2386192, 0.2386192, 0.6612094, 0.9324695]
]

Ak = [
    [2.0000000],
    [1.0000000, 1.0000000],
    [0.5555556, 0.8888889, 0.5555556],
    [0.3478548, 0.6521452, 0.6521452, 0.3478548],
    [0.2369269, 0.4786287, 0.5688889, 0.4786287, 0.2369269],
    [0.1713245, 0.3607616, 0.4679139, 0.4679139, 0.3607616, 0.1713245]
]


# 复合高斯公式
def Compound_Goss(point, f, begin=-1.0, end=1.0, n=1):
    # 根据传入参数确定是哪种高斯公式，选择对应的Xk和Ak值
    x = Xk[point]
    A = Ak[point]

    # 计算间隔h
    h = (end - begin) / n
    # print h
    I = np.zeros(n, dtype=np.float64)
    for i in range(n):
        a = begin + i * h
        b = begin + (i + 1) * h
        # print a,b
        I[i] = sum([f(change(a, b, x[k])) * A[k] for k in range(len(x))])
        I[i] *= (b - a) / 2
    return sum(I)
