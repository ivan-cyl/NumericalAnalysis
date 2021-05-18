import numpy as np

n = 10


def Jacobi(A, b, x0, xstar):
    k = 0
    while True:
        for i in range(0, n):
            sum = 0.0
            for j in range(0, i):
                sum = sum + A[i][j] * x0[j]
            for j in range(i + 1, n):
                sum = sum + A[i][j] * x0[j]
            xstar[i] = (b[i] - sum) / A[i][i]
        temp = np.fabs(xstar[0] - x0[0])
        for j in range(1, n):
            if np.fabs(xstar[j] - x0[j]) > temp:
                temp = np.fabs(xstar[j] - x0[j])
        for j in range(0, n):
            x0[j] = xstar[j]
        k = k + 1
        if (temp < 1.0e-6 or k > 1000):
            break
    print("Jacobi:", k)

