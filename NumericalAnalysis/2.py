def difference_quotient_list(y_list, x_list):
    if x_list == []:
        x_list = [i for i in range(len(y_list))]
    # print(y_list)
    prev_list = y_list
    dq_list = []
    dq_list.append(prev_list[0])
    for t in range(1, len(y_list)):
        prev, curr = 0, 0
        m = []
        k = -1
        for i in prev_list:
            curr = i
            m.append((curr - prev) / (x_list[k + t] - x_list[k]))
            prev = i
            k += 1
        m.pop(0)
        prev_list = m
        dq_list.append(prev_list[0])
        # print(m)
    return dq_list


def newton_interpolate(x_list, y_list, x):
    coef = difference_quotient_list(y_list, x_list)
    p = coef[0]
    for i in range(1, len(coef)):
        product = 1
        for j in range(i):
            product *= (x - x_list[j])
        p += coef[i] * product
    return p


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from dateutil.parser import parse


    plt.rcParams['font.sans-serif'] = ['STZhongsong']  # 指定默认字体：解决plot不能显示中文问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    # 待插值的元素值
    x0 = [1, 15, 22]
    y0 = [0, 0, 0]
    t1 = [parse('2021-10-01/6:9:00'), parse('2021-10-15/6:31:00'), parse('2021-10-22/6:23:00')]
    t2 = [parse('2021-10-01/17:36:00'), parse('2021-10-15/17:58:00'), parse('2021-10-22/17:26:00')]
    for i in range(3):
        y0[i] = (t2[i] - t1[i]).seconds
    # 牛顿插值
    x = np.linspace(1, 30)
    y = list(map(lambda t: newton_interpolate(x0, y0, t), x))

    # 画图
    plt.scatter(x0, y0, color="orange")
    plt.plot(x, y)
    plt.xlabel("日期/天")
    plt.ylabel("日照时间/s")
    plt.title("Newton插值法")
    plt.savefig("D:/Desktop/数值分析/图片/#2.png")

    m, s = divmod(newton_interpolate(x0, y0, 8), 60)
    h, m = divmod(m, 60)

    print("当年10月8日北京市的日照时长为%02d小时%02d分%02d秒" % (h, m, s))
