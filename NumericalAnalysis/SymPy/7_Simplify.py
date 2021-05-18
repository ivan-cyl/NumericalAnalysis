from sympy import sin, cos, simplify, pprint
from sympy.abc import x

expr = sin(x) / cos(x)

pprint(expr)

print('-----------------------')

expr = simplify(expr)
# 可以使用simplify()将表达式更改为更简单的形式

pprint(expr)
