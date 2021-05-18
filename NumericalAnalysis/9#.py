# 用Newton法求x - tanx = 0的最小正根
from sympy import *
import numpy as np


# 1.定义原方程
def f(x):
    return x ** 3 + 2 * x ** 2 + 10 * x - 20


# 2.定义函数求导公式
def sympy_derivative(f):
    x = symbols('x')  # 定义符号变量
    # 定义表达式内容
    Y = f(x)
    # 计算 x的导数
    return diff(Y, x)


# 3.定义迭代公式
def f_1(x):
    return float(20 / (x ** 2 + 2 * x + 10))


def f1(x0):
    x = symbols('x')  # 定义符号变量
    # 定义表达式内容
    F = f(x)
    return float(diff(F,x).evalf(subs={'x': x0}))


# 3.定义迭代公式
def f_2(x):
    return float((20 - 2 * x ** 2 - x ** 3) / 10)


# 4.控制、修改
def Newton(x0, epsilon, f, f1):
    n = 0
    while True:
        if n < 20:
            n = n + 1
            x1 = f1(x0)
            if abs(f(x1)) > abs(f(x0)):
                print('因为不满足单调性，需要另选初值x0计算')
                break
            x0 = x1
            print('迭代次数：', "{0:.0f}".format(n),
                  '迭代后的值：', " {0:.9f}".format(x1))

            if x1 < epsilon:
                print('迭代最终次数：', "{0:.0f}".format(n),
                      '牛顿法求得方程的根：', " {0:.9f}".format(x1))
                break
            x0 = x1
            print('迭代次数：', "{0:.0f}".format(n),
                  '迭代后的值：', " {0:.9f}".format(x1))
        else:
            break

def newton(x0, epsilon, iternum,f,f1):
    """
    牛顿迭代法x = x - f(x)/f'(x)
    x0:初值, N:最大迭代次数, eps:根误差限
    """
    for k in range(0,iternum,1):
        x = x0 - f(x0) / f1(x0)
        print(x)
        if np.abs(x) < 1:
            if np.abs(x-x0) < epsilon:
                print(f"经过{k+1:d}次迭代，初值为{x0:f}的根为{x:.9f}, 此时函数值为{f(x):.9f}")
                return (x,k, f(x))
        else:
            if np.abs(x-x0)/np.abs(x) < epsilon:
                print(f"经过{k+1:d}次迭代，初值为{x0:f}的根为{x:.9f}, 此时函数值为{f(x):.9f}")
                return (x,k, f(x))
        x0 = x
    print(f"迭代超过{N:d}次，迭代失败")


# 5.调用迭代函数


# Newton(x0, eps, f, f_1)  # 调用函数进行迭代
# Newton(x0, eps, f, f_2)  # 调用函数进行迭代


# ---------------------------------------------------------------------------------------

def Aitken(x0, epsilon, iternum, f):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    for i in range(iternum):
        y = f(xk_1)
        z = f(y)
        if (z - 2 * y + xk_1) != 0:
            xk = xk_1 - (y - xk_1) ** 2 / (z - 2 * y + xk_1)
            print(f"第{i+1:d}次迭代  ，xk={xk:.9f}  xk-1={xk_1:.9f}  |xk - xk-1|={abs(xk - xk_1):.9f}")
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            return xk
    print("方法失败")
    return 0


# Aitken(x0, eps, 100, f_1)
# Aitken(x0, eps, 100, f_2)


# ----------------------------------------------------------------------------------------------------------

def Iterative(x0, epsilon, iternum, f):
    x = np.array([x0])  # x0
    x = np.append(x, f(x[0]))  # x1
    print(f"x[0] = {x[0]:.9f}")
    print(f"x[1] = {x[1]:.9f}, 误差为{np.abs(x[1] - x[0]):.8f}")
    k = 1
    while (np.abs(x[k] - x[k - 1]) > epsilon):
        x = np.append(x, f(x[k]))  # x_k+1
        print(f"x[{k + 1:d}] = {x[k + 1]:.9f}, 误差为{np.abs(x[k + 1] - x[k]):.9f}")
        k += 1;
        if k > iternum:
            break
    print(f"根为x[{k:d}] = {x[k]:.9f}")
    print("共迭代了%d次达到精度要求" % k)



# Iterative(f_1)
# Iterative(f_2)
if __name__ == '__main__':
    eps = 1e-9  # 设定误差限
    x0 = 1  # 设定初值
    #Newton(1.5, eps, f, f1)  # 调用函数进行迭代
    print("第一个迭代公式迭代法：")
    Iterative(x0, eps, 100, f_1)
    print("第二个迭代公式迭代法：")
    Iterative(1, eps, 100, f_2)
    print("第一个迭代公式Aitken加速方法：")
    Aitken(x0, eps, 100, f_1)
    print("第二个迭代公式Aitken加速方法：")
    Aitken(x0, eps, 100, f_2)
    #print(sympy_derivative(f))
    print("Newton法：")
    newton(x0, eps, 100,f, f1)