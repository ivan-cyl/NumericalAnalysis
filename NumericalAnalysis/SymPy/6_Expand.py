from sympy import expand, pprint
from sympy.abc import x

expr = (x + 1) ** 2

pprint(expr)

print('-----------------------')
print('-----------------------')

expr = expand(expr)
# 使用expand()，我们可以扩展代数表达式； 即该方法尝试消除幂和乘法
pprint(expr)