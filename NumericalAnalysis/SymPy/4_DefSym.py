from sympy import Symbol, symbols
from sympy.abc import x, y

# sympy.abc模块导入符号。 它将所有拉丁字母和希腊字母导出为符号，因此我们可以方便地使用它们

expr = 2 * x + 5 * y
print(expr)

# 可以用Symbol定义
a = Symbol('a')
b = Symbol('b')

expr2 = a * b + a - b
print(expr2)

i, j = symbols('i j')
# 可以使用symbols()方法定义多个符号
expr3 = 2 * i * j + i * j
print(expr3)
