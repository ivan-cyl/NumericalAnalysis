# 参考精确值x_prec计算x_appr的位数
def significant_figures(x_appr, x_prec):
    p = 0  # the order of the approximated number
    n = 0
    # 以下把x_appr化成规格化浮点数，计算阶数 p
    x = x_appr
    while x >= 1:
        x /= 10
        p += 1
    while x < 0.1:
        x *= 10
        p -= 1

    d = abs(x_appr - x_prec)
    while True:
        n += 1
        if d > 0.5 * 10 ** (p - n):
            break

    return n - 1


print("3.14相对于pi有效数字为",significant_figures(3.14, 3.1415926))  # 打印结果为3
