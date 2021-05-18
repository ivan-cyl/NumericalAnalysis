def Aitken(x0, epsilon, iternum, phi):  # 初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    for i in range(iternum):
        y = phi(xk_1)
        z = phi(y)
        if (z - 2 * y + xk_1) != 0:
            xk = xk_1 - (y - xk_1) ** 2 / (z - 2 * y + xk_1)
            print("第", i + 1, "次迭代 ", "xk=", xk, "  xk-1=", xk_1, "  |xk - xk-1|=", abs(xk - xk_1));
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            return xk
    print("方法失败")
    return 0
