from sympy import pi

# 可以通过替换符号来求值表达式
# https://docs.sympy.org/latest/modules/evalf.html
print(pi.evalf(30))
# 将 pi 值求值为 30 个位


from sympy.abc import a, b

expr = b * a + -4 * a + b + a * b + 4 * a + (a + b) * 3
# 用数字替换a和b符号来求值表达式
print(expr.subs([(a, 3), (b, 2)]))
