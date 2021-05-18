import numpy as np

# 传入插值节点序列x、原函数f、导函数f_和样条插值的类别，生成三次样条插值函数
def Cubic_Spline(xi, f, f_, kind):
    yi = f(xi)
    y_i = f_(xi)


    # 根据公式求出4个参数
    h = np.array([xi[k+1]- xi[k] for k in range(len(xi) - 1)],dtype = np.float32)
    u = np.array([h[k-1]/(h[k-1] + h[k]) for k in range(len(h) - 1)] + [1.0])
    lam = np.array([1.0] + [h[k]/(h[k-1] + h[k]) for k in range(len(h) - 1)])

    n = len(xi)
    d = np.zeros(n) + 1
    dyi = np.array([(yi[k+1] - yi[k])/h[k] for k in range(len(xi) - 1)])
    for j in range(1,n - 1):
        d[j] = 6 * (dyi[j] - dyi[j - 1])/(h[j-1] +h[j] )

    #根据参数判断是第几类样条插值
    #第一类则使用题目给定的两端点一次导数值
    if kind == 'first':
        d[0] = 6/h[0] * (dyi[0] - 1)
        d[-1] = 6/h[-1] * (1 - dyi[-1])
     #第二类则使用原函数两端点一次导数值
    else:
        d[0] = 6/h[0] * (dyi[0] - y_i[0])
        d[-1] = 6/h[-1] * (y_i[-1] - dyi[-1])

    # 利用矩阵运算得出M
    A = np.mat(np.eye(n,n)) * 2.0
    for i in range(n-1):
        A[i + 1,i] = u[i]
        A[i,i+1] = lam[i]

    B = np.matrix(d)
    B = B.T

    M =  A.I * B
    M = np.array(M.T[0])[0]

    # 生成三次样条插值函数
    def Sx(x):
        result = 0.0
        # 利用k来定位x所处的区间
        k = 0
        while k < n and not (xi[k] <= x and xi[k+1] >= x):
            k += 1
        result = M[k] * (xi[k+1] - x)**3 / (6*h[k]) + M[k+1] * (x - xi[k])**3 / (6*h[k]) +\
            (yi[k] - (M[k]*h[k]**2)/6) * ((xi[k+1] - x) / h[k]) + \
            (yi[k+1] - (M[k+1]*h[k]**2)/6) * ((x - xi[k])/h[k])
        return result
    return Sx