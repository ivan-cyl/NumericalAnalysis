# 传入插值节点序列x和原函数f，获取分段线性插值函数
def subLiner(xi, f):
    yi = f(xi)

    def Lh(x):
        result = 0.0
        # 利用k来定位x所处的区间
        k = 0
        while k < len(xi) and not (xi[k] <= x and xi[k+1] >= x):
            k += 1
        result = (x - xi[k+1])/(xi[k] - xi[k+1]) * yi[k] + \
            (x - xi[k])/(xi[k+1] - xi[k]) * yi[k+1]
        return result
    return Lh


#---------------------------------------------------------------

# 分段线性插值，需要两个列表
def segmented_linear_interpolate(xlist,ylist,x):
    """
    n = # of intervals, which is derived from len of xlist
    len of xlist is always one item biger than # of intervals
    """
    # we have to make sure that items in xlist is in order
    data = dict(zip(xlist,ylist))
    # 按照key排序，也就是xlist
    data = sorted(data.items(),key=lambda item:item[0])
    data = dict(data)
    xlist = list(data.keys())
    ylist = list(data.values())
    n = len(xlist)-1
    if n == 0:
        raise ValueError("n should be greater or equal to 1")
    # print("segmented interpolate, n =",n)
    # 需要把新来的元素判断一下在哪个区间
    i = -1
    for t in xlist:
        if x >= t:
            i += 1
    if i == -1 or i > len(xlist)-1:
        raise ValueError("x should be between %f and %f"%(xlist[0],xlist[-1]))
    if i == len(xlist)-1:
        return ylist[i]
    return (x-xlist[i+1])/(xlist[i]-xlist[i+1])*ylist[i] + (x-xlist[i])/(xlist[i+1]-xlist[i])*ylist[i+1]


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    f = lambda x: 1/(1+25*x**2)
    # 待插值的元素值
    x_points = [0,1,2,3,4]
    y_points = [20,18,10,2,1]

    # 分段线性插值
    f = lambda t: segmented_linear_interpolate(x_points,y_points,t)
    x = np.linspace(0,4)
    y = list(map(f,x))
    # 画图
    plt.figure("segmented linear interpolation")
    plt.scatter(x_points,y_points,color = "orange")
    plt.plot(x,y)
    plt.legend(["segmented linear interpolation","scattered points"])
    plt.show()

    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: 1 / (1 + 25 * x ** 2)
    # 待插值的元素值
    x_points = np.linspace(-1, 1, 11)
    y_points = list(map(f, x_points))

    # 分段线性插值
    fx = lambda t: segmented_linear_interpolate(x_points, y_points, t)
    x = np.linspace(-1, 1, 51)
    y = list(map(fx, x))
    # 画图
    plt.figure("segmented interpolation")
    plt.scatter(x_points, y_points, color="orange")
    plt.plot(x, y)
    plt.legend(["segmented interpolation", "scattered points"])
    plt.show()