import numpy as np
import matplotlib.pyplot as plt


def Lagrange(x, f):
    def lx(xi):
        result = 0.0
        for i in range(len(x)):
            tmp = f[i]
            for j in range(len(f)):
                if i != j:
                    tmp *= (xi - x[j]) / (x[i] - x[j])
            result += tmp
        return result

    return lx


def lagrange(x, y, x_test):
    l = np.zeros(shape=(len(x)))
    # 构建0构建已有离散点数量的0数组
    L = 0
    for i in range(len(x)):
        # 计算基函数的值
        l[i] = 1
        for j in range(len(x)):
            if i != j:
                l[i] = l[i] * (x_test - x[j]) / (x[i] - x[j])
            else:
                pass
        L += y[j] * l[j]
        # 求所有基函数值的和
    return L


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
    np.linalg.solve()
    val = p(x, a)
    print(x, val)
    return val


if __name__ == '__main__':
    x = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    y = [14, 7, 5, 1, 2, 6, 7, 8, 13, 20, 21]
    # 所测的不足的离散点

    Lagrange(x, y)

    x_test = list(np.linspace(-3, 7, 50))
    y_predict = [lagrange(x, y, x_i) for x_i in x_test]
    # 进行插值，但插值数量不能过大，否则会造成龙格现象
    # 在数值分析领域中，龙格现象是在一组等间插值点上使用具有高次多项式的多项式插值时出现的区间边缘处的振荡问题。 它是由卡尔·龙格（Runge）在探索使用多项式插值逼近某些函数时的错误行为时发现的。它表明使用高次多项式插值并不总能提高准确性。 该现象与傅里叶级数近似中的吉布斯现象相似。

    x_points = [0, 1, 2, 3, 4, 5]
    y_points = [1, 5, 4, 8, 7, 12]
    # 拉格朗日插值
    x = np.linspace(0, 5)
    y = list(map(lambda t: lagrange_interpolate(x_points, y_points, t), x))
    # 画图
    plt.scatter(x_points, y_points, color="orange")
    plt.plot(x, y)
    plt.legend(["lagrange interpolation", "scattered points"])
    plt.show()
