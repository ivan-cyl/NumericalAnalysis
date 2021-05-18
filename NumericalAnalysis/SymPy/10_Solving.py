from sympy import Symbol, solve

x = Symbol('x')

sol = solve(x ** 2 - x, x)
# 使用solve()解决了一个简单方程
# solve()的第一个参数是公式。 该公式以适合 SymPy 的特定形式编写； 即x**2 - x代替x**2 = x。 第二个参数是我们需要解决的符号
print(sol)

from sympy import pprint, Symbol, Eq, solve

x = Symbol('x')

eq1 = Eq(x + 1, 4)
# 将Eq用于公式
pprint(eq1)

sol = solve(eq1, x)
print(sol)

from sympy.solvers import solveset
from sympy import Symbol, Interval, pprint

x = Symbol('x')

sol = solveset(x ** 2 - 1, x, Interval(0, 100))
# 使用solveset()，我们找到了给定间隔的解决方案
pprint(sol)
