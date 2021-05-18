from sympy import pprint, Symbol, sin, cos

x = Symbol('x')

a = cos(x) ** 2 - sin(x) ** 2
b = cos(2 * x)

print(a.equals(b))
# SymPy 表达式与equals()而不是==运算符进行比较

# 不能使用==来完成比较表达式
print(a == b)
