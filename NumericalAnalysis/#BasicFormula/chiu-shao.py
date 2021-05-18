import numpy as np


def shao_cal(in_x, sums, point):
    lenth = len(sums)
    result = sums[lenth - 1]
    result = np.around(result, decimals=3)
    for i in range(1, lenth):
        result = result * (in_x - point) + sums[lenth - i - 1]
        result = np.around(result, decimals=3)
    return result
