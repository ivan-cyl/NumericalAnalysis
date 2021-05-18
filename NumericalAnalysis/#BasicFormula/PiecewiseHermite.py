# 传入插值节点序列x、原函数f和导函数f_，生成分段埃尔米特插值函数
def subHermite(xi, f, f_):
    yi = f(xi)
    y_i = f_(xi)

    def lh(x):
        result = 0.0
        # 利用k来定位x所处的区间
        k = 0
        while k < len(xi) and not (xi[k] <= x and xi[k + 1] >= x):
            k += 1
        result = ((x - xi[k + 1]) / (xi[k] - xi[k + 1])) ** 2 * (1 + 2 * (x - xi[k]) / (xi[k + 1] - xi[k])) * yi[k] + \
                 ((x - xi[k]) / (xi[k + 1] - xi[k])) ** 2 * (1 + 2 * (x - xi[k + 1]) / (xi[k] - xi[k + 1])) * yi[
                     k + 1] + \
                 ((x - xi[k + 1]) / (xi[k] - xi[k + 1])) ** 2 * (x - xi[k]) * y_i[k] + \
                 ((x - xi[k]) / (xi[k + 1] - xi[k])) ** 2 * (x - xi[k + 1]) * y_i[k + 1]
        return result

    return lh


# ----------------------------------------------------------------

# 分段Hermite插值，需要输入三个列表
def segmented_hermite_interpolate(x_list, y_list, y_prime_list, x):
    """
    n = # of intervals, which is derived from len of xlist
    len of xlist is always one item biger than # of intervals
    """
    # we have to make sure that items in xlist is in order

    # 按照x_list给y_list排序
    data = dict(zip(x_list, y_list))
    data = sorted(data.items(), key=lambda item: item[0])
    data = dict(data)
    xlist = list(data.keys())
    ylist = list(data.values())
    # 按照x_list给y_prime_list排序
    data = dict(zip(x_list, y_prime_list))
    data = sorted(data.items(), key=lambda item: item[0])
    data = dict(data)
    y_prime_list = list(data.values())

    n = len(xlist) - 1
    if n == 0:
        raise ValueError("n should be greater or equal to 1")
    # print("segmented interpolate, n =",n)
    # 需要把新来的元素判断一下在哪个区间
    i = -1
    for t in xlist:
        if x >= t:
            i += 1

    if i == -1 or i > len(xlist) - 1:
        raise ValueError("x should be between %f and %f" % (xlist[0], xlist[-1]))
    if i == len(xlist) - 1:
        return ylist[i]

    alpha0 = lambda x: ((x - xlist[i + 1]) / (xlist[i] - xlist[i + 1])) ** 2 * (
            2 * (x - xlist[i]) / (xlist[i + 1] - xlist[i]) + 1)
    alpha1 = lambda x: ((x - xlist[i]) / (xlist[i + 1] - xlist[i])) ** 2 * (
            2 * (x - xlist[i + 1]) / (xlist[i] - xlist[i + 1]) + 1)
    beta0 = lambda x: ((x - xlist[i + 1]) / (xlist[i] - xlist[i + 1])) ** 2 * (x - xlist[i])
    beta1 = lambda x: ((x - xlist[i]) / (xlist[i + 1] - xlist[i])) ** 2 * (x - xlist[i + 1])
    H = alpha0(x) * ylist[i] + alpha1(x) * ylist[i + 1] + beta0(x) * y_prime_list[i] + beta1(x) * y_prime_list[i + 1]
    return H


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    # 待插值的元素值
    x_points = [0, 1, 2, 3, 4]
    y_points = [5, 4, 3, 2, 1]
    y_primes = [0, 0, 0, 0, 0]  # 让各点导数等于0

    # 分段hermite插值
    f = lambda t: segmented_hermite_interpolate(x_points, y_points, y_primes, t)
    x = np.linspace(0, 4)
    y = list(map(f, x))
    # 画图
    plt.figure("segmented hermite interpolation")
    plt.scatter(x_points, y_points, color="orange")
    plt.plot(x, y)
    plt.legend(["segmented hermite interpolation", "scattered points"])
    plt.show()
