from sympy import Rational

# https://docs.sympy.org/latest/modules/evalf.html

# 有理数是可以表示为两个整数（分子 p 和非零分母 q）的商或分数 p / q 的任何数字

r1 = Rational(1 / 10)
r2 = Rational(1 / 10)
r3 = Rational(1 / 10)
# evalf()函数可以用求出表达式的浮点数

val = (r1 + r2 + r3) * 3
print(val.evalf())

val2 = (1 / 10 + 1 / 10 + 1 / 10) * 3
print(val2)
