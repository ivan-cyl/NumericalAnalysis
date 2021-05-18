# 生成朗格朗日基函数
def get_li(i, x_all):
    def li(xx):
        a = 1.0
        b = 1.0
        for j in range(len(x_all)):
            if j == i:
                continue
            a *= (xx - x_all[j])
            b *= (x_all[i] - x_all[j])
        return a / b

    return li


# 求alpha基函数
def get_alpha(i, x_all=[]):
    def alpha(xx):
        result = 0.0
        for k in range(len(x_all)):
            if k == i:
                continue
            result += 1.0 / (x_all[i] - x_all[k])
        result = (1 + 2 * (x_all[i] - xx) * result)
        li = get_li(i, x_all)
        result *= li(xx) ** 2
        return result

    return alpha


# 求alpha基函数
def get_beta(i, x_all=[]):
    def beta(xx):
        li = get_li(i, x_all)
        result = (xx - x_all[i]) * li(xx) ** 2
        return result

    return beta


def Hermite(x, f, f_):
    # 分别对应x，y，对应x的导数
    def He(xi):
        result = 0.0
        n = len(x)
        for i in range(n):
            ai = get_alpha(i, x)
            # 求出a
            bi = get_beta(i, x)
            # 求出b
            result += f[i] * ai(xi) + f_[i] * bi(xi)
        return result

    return He


def hermite(x0, x1, y0, y1, y0_prime, y1_prime, x):
    alpha0 = lambda x: ((x - x1) / (x0 - x1)) ** 2 * (2 * (x - x0) / (x1 - x0) + 1)
    alpha1 = lambda x: ((x - x0) / (x1 - x0)) ** 2 * (2 * (x - x1) / (x0 - x1) + 1)
    beta0 = lambda x: ((x - x1) / (x0 - x1)) ** 2 * (x - x0)
    beta1 = lambda x: ((x - x0) / (x1 - x0)) ** 2 * (x - x1)
    H = alpha0(x) * y0 + alpha1(x) * y1 + beta0(x) * y0_prime + beta1(x) * y1_prime
    return H


# ------------------------------------------------------------

# 返回多项式
def p(x, a):
    """
    p(x,a)是x的函数，a是各幂次的系数
    """
    s = 0
    for i in range(len(a)):
        s += a[i] * x ** i
    return s


# n次拉格朗日插值
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


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: hermite(0, 1, 0, 1, -1, -4, x)
    x = np.linspace(0, 1)
    y = list(map(f, x))
    plt.scatter([0, 1], [0, 1], color="orange")
    plt.plot(x, y)
    plt.show()

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
