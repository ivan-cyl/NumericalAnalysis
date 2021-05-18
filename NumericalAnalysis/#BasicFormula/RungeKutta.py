# 自行更改微分方程
def f(p, q):
    return (-1) * q - p * q ** 2


# 把公式拆分更简洁
def zsj(m, n, h):
    K1 = f(m, n)
    K2 = f(m + h * 0.5, n + h * 0.5 * K1)
    K3 = f(m + h * 0.5, n + h * 0.5 * K2)
    K4 = f(m + h, n + h * K3)
    return K1 + 2 * K2 + 2 * K3 + K4


# f=微分方程；求解区间(a,b)；ya=y(0),h=步长
def LB(f, a, b, ya, h):
    xi = a
    while xi <= b:
        if xi == 0:
            yi = ya
        else:
            yi = yi + h / 6 * zsj(xi - 0.2, yi, h)
        print('y(%s)= %s' % (xi, yi))
        xi = xi + h


print(LB(f, 0, 1, 1, 0.2))


# --------------------------------------------------------
# 返回多项式
def p(x, a):
    """
    p(x,a)是x的函数，a是各幂次的系数
    """
    s = 0
    for i in range(len(a)):
        s += a[i] * x ** i
    return s


def lagrange_interpolate(x_list, y_list, x):
    """
    x_list 待插值的x元素列表
    y_list 待插值的y元素列表
    插值以后整个lagrange_interpolate是x的函数
    """
    if len(x_list) != len(y_list):
        raise ValueError("list x and list y is not of equal length!")
    # 系数矩阵
    A = []
    for i in range(len(x_list)):
        A.append([])
        for j in range(len(x_list)):
            A[i].append(pow(x_list[i], j))
    b = []
    for i in range(len(x_list)):
        b.append([y_list[i]])
    # 求得各阶次的系数
    a = np.linalg.solve(A, b)  # 用LU分解法解线性方程组，可以使用numpy的类似函数
    a = np.transpose(a)[0]  # change col vec a into 1 dimension
    val = p(x, a)
    print(x, val)
    return val


# 龙格现象的产生
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: 1 / (1 + 25 * x ** 2)
    # 待插值的元素值
    x_points = np.linspace(-1, 1, 11)
    print(x_points)
    y_points = list(map(f, x_points))
    # 牛顿插值
    x = np.linspace(-1, 1)
    y = list(map(lambda t: lagrange_interpolate(x_points, y_points, t), x))
    # 画图
    plt.figure("lagrange interpolation")
    plt.scatter(x_points, y_points, color="orange")
    plt.plot(x, y)
    plt.legend(["lagrange interpolation", "scattered points"])
    plt.show()
