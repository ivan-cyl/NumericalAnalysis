def Euler(x_0, y_0, h, f, f_1):    # 构造Euler公式
    yn = y_0
    xn = x_0
    for n in range(1, 11):
        x = xn + h*n
        yp = yn + h*f(xn, yn)
        yc = yn + h*f(x, yp)
        y = (yp + yc)/2
        yn = f_1(x)            # 计算准确值
        eps = abs(yn - y)
        print('迭代次数：', "{0:.0f}".format(n),
              '迭代后x值：', "{0:.4f}".format(x),
              '迭代后y值：', "{0:.4f}".format(y),
              'y的精确值：', "{0:.4f}".format(yn),
              '误差：', "{0:.4f}".format(eps))
        if x == 0.5:
            print('y(0.5)=', "{0:.4f}".format(y))
