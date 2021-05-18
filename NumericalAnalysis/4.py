# 自行更改微分方程
def f(x, y):
    return y - 2 * x / y


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


# ---------------------------------------------------------------------------------------

# 导入包
import numpy as np
import matplotlib.pyplot as plt


# 定义求解函数 y_dot = y + 2*x/(y*y)
def fx(y, x):
    return y + 2 * x / (y * y)


# 算法定义
def ode_euler(f, y0, tf, h):
    """
    Solve and ODE using Euler method.
    Solve the ODE y_dot = f(y, t)
    Parameters
    ------------
    :param f: function
            Function describing the ODE
    :param y0: array_like
            Initial conditions.
    :param tf: float
            Final time.
    :param h: float
            Time step
    :return:
    y : array_like
        Solution to the ODE.
    t : array_like
        Time vector.
    """

    y0 = np.array(y0)
    ts = np.arange(0, tf + h, h)
    y = np.empty((ts.size, y0.size))
    y[0, :] = y0
    for t, i in zip(ts[1:], range(ts.size - 1)):
        y[i + 1, :] = y[i, :] + h * f(y[i, :], t)
    return y, ts


# 实例应用案例
def newton_cooling_example():
    print('Solving Newton Cooling ODE...')
    y, ts = ode_euler(fx, 1, 2, 0.01)
    print('Done.')
    plt.figure()
    plt.plot(ts, y)
    plt.xlabel('time [s]')
    plt.title('Solution to the Newton cooling equation')
    plt.show()


if __name__ == '__main__':
    print(LB(f, 0, 1, 1, 0.1))
