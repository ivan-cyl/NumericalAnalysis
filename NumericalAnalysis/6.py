import numpy as np


def Fx1(x):
    '''迭代函数. 收敛性由定理2保证.'''
    return (0.5 * (3 + np.sin(x) - 1 - x ** 2))


def Iterative(x0, epsilon, iternum, f):
    x = np.array([x0])  # x0
    x = np.append(x, f(x[0]))  # x1
    print(f"x[0] = {x[0]:.8f}")
    print(f"x[1] = {x[1]:.8f}, 误差为{np.abs(x[1] - x[0]):.8f}")
    k = 1
    while (np.abs(x[k] - x[k - 1]) > epsilon):
        x = np.append(x, f(x[k]))  # x_k+1
        print(f"x[{k + 1:d}] = {x[k + 1]:.8f}, 误差为{np.abs(x[k + 1] - x[k]):.8f}")
        k += 1;
        if k > iternum:
            break
    print(f"根为x[{k:d}] = {x[k]:.8f}")
    print("共迭代了%d次达到精度要求" % k)


if __name__ == "__main__":
    eps = 1e-2
    it = 100
    Iterative(0.25, eps, it, Fx1)
