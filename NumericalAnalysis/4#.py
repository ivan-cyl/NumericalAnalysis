import warnings

warnings.filterwarnings('ignore')


def f(x, y):
    '''
    求解的微分方程，
    '''
    return y - 2 * x / y


def ft(x):
    '''
    求解的微分方程，
    '''
    return (1 + 2 * x) ** 0.5


def euler_forward(f, a=0, b=1, ya=1, h=0.1, verbose=True):
    '''向前欧拉法
    Args
    ----------
    f： callable function
        需要求解的函数
    a: float
        求解区间起始值
    b：float
        求解区间终止值
    ya：float
        起始条件，ya=y(a)
    h：float
        求解步长（区间[a,b]n等分）
    verbose：logical，default is True
        显示迭代结果

    Returns
    ----------
    res：list like
        返回向前欧拉发求解的结果
    '''
    #     i = 0
    res = []
    xi = a
    yi = ya

    print("欧拉法:")
    while xi <= b:  # 在求解区间范围
        y = yi + h * f(xi, yi)
        if verbose:
            print('xi:{:.2f}, yi:{:.6f}'.format(xi, yi))
        res.append(y)
        xi, yi = xi + h, y

    return res


def runge_kutta(f, a=0, b=1, ya=1, h=0.1, verbose=True):
    '''四阶龙格库塔法
    Args
    ----------
    f： callable function
        需要求解的函数
    a: float
        求解区间起始值
    b：float
        求解区间终止值
    ya：float
        起始条件，ya=y(a)
    h：float
        求解步长（区间[a,b]n等分）
    verbose：logical，default is True
        显示迭代结果

    Returns
    ----------
    res：list like
        返回向前欧拉发求解的结果
    '''
    res = []
    xi = a
    yi = ya

    print("四阶龙格库塔法:")
    while xi <= b:  # 在求解区间范围
        k1 = h * f(xi, yi)
        k2 = h * f(xi + h / 2, yi + k1 / 2)
        k3 = h * f(xi + h / 2, yi + k2 / 2)
        k4 = h * f(xi + h, yi + k3)
        y = yi + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if verbose:
            print('xi:{:.2f}, yi:{:.6f}'.format(xi, yi))
        res.append(y)
        xi, yi = xi + h, y

    return res


def improved_euler(f, a=0, b=1, ya=1, h=0.1, verbose=True):
    '''改进欧拉法
    Args
    ----------
    f： callable function
        需要求解的函数
    a: float
        求解区间起始值
    b：float
        求解区间终止值
    ya：float
        起始条件，ya=y(a)
    h：float
        求解步长（区间[a,b]n等分）
    verbose：logical，default is True
        显示迭代结果

    Returns
    ----------
    res：list like
        返回向前欧拉发求解的结果
    '''
    res = []
    xi = a
    yi = ya

    print("改进欧拉法:")
    while xi <= b:  # 在求解区间范围
        yp = yi + h * f(xi, yi)
        y = yi + h / 2 * (f(xi, yi) + f(xi, yp))
        if verbose:
            print('xi:{:.2f}, yi:{:.6f}'.format(xi, yi))
        res.append(y)
        xi, yi = xi + h, y

    return res


def precise(f, a=0, b=1, ya=1, h=0.1, verbose=True):
    '''改进欧拉法
        Args
        ----------
        f： callable function
            需要求解的函数
        a: float
            求解区间起始值
        b：float
            求解区间终止值
        ya：float
            起始条件，ya=y(a)
        h：float
            求解步长（区间[a,b]n等分）
        verbose：logical，default is True
            显示迭代结果

        Returns
        ----------
        res：list like
            返回向前欧拉发求解的结果
        '''
    res = []
    xi = a
    yi = ya

    print("精确值:")
    while xi <= b:  # 在求解区间范围
        yi = ft(xi)
        if verbose:
            print('xi:{:.2f}, yi:{:.6f}'.format(xi, yi))
        res.append(yi)
        xi += h

    return res


if __name__ == '__main__':
    euler_forward(f, 0, 1, 1, 0.1)
    runge_kutta(f, 0, 1, 1, 0.1)
    improved_euler(f, 0, 1, 1, 0.1)
    precise(ft, 0, 1, 1, 0.1)
