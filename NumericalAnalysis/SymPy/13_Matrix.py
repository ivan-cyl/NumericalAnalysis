from sympy import Matrix, pprint

# 使用矩阵。 矩阵是数字或其他数学对象的矩形数组，为其定义了运算（例如加法和乘法）

M = Matrix([[1, 2], [3, 4], [0, 3]])
print(M)
pprint(M)

N = Matrix([2, 2])

print("---------------------------")
print("M * N")
print("---------------------------")

pprint(M * N)
