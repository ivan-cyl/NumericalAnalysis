# 近似，舍掉的那部分叫做模型误差；数据观测是有误差的，叫做观测误差，二者不属于我们研究的对象
import sympy as sp

# 虚数单位
print(sp.I ** 2)

# 科学常数
print(sp.E)

# 无穷大
print(1 / sp.oo)

# pi
print(sp.pi)

# 开方
print(sp.sqrt(-1))

# 对数运算,写一项时默认以e为基地
print(sp.log(1000, 10))

# 开根号
print(sp.root(8, 3))

# 阶乘
print(sp.factorial(10))

# 三角函数,此处以sin为例
print(sp.sin(sp.pi))

x = sp.Symbol('x')
fx = 2 * x + 1
print(fx.evalf(subs={x: 2}))

# 导入多个
i, j = sp.symbols('i j')
gx = i + j
sp.pprint(gx.evalf(subs={i: 1, j: 2}))
# 从sympy.abc导入
from sympy.abc import x, y

hx = x / y
sp.pprint(hx.evalf(subs={x: 1, y: 2}))

r = sp.Rational(1 / 10)
val = 3 * r
sp.pprint(val.evalf())
sp.pprint(1 / 10 * 3)
# pprint可用于美化输出，类似于latex的输出,某些字符maybe需要unicode编码支持

sp.init_printing(use_unicode=True)
x = sp.Symbol('x')
c = (sp.exp(x) ** 2 + 1 / x)
print(c)
sp.pprint(c)

# 自动规范表达式
from sympy.abc import a, b

expr = b * a + -4 * a + b + a * b + 4 * a + (a + b) * 3
sp.pprint(expr)

# 展开表达式
expr = (x + 1) ** 2
sp.pprint(sp.expand(expr))

# 简化表达式
expr = sp.sin(x) / sp.cos(x)
sp.pprint(sp.simplify(expr))

# 比较表达式
a = sp.cos(x) ** 2 - sp.sin(x) ** 2
b = sp.cos(2 * x)
print(a.equals(b))

# 通过替换值来求表达式
from sympy.abc import a, b

expr = b * a + -4 * a + b + a * b + 4 * a + (a + b) * 3
sp.pprint(expr.subs([(a, 3), (b, 2)]))

# 求解方程
x = sp.Symbol('x')
sol = sp.solve(x ** 2 - x, x)
print(sol)

# 或者写成公式的形式
eq1 = sp.Eq(x + 1, 4)
sp.pprint(eq1)
sol = sp.solve(eq1, x)
print(sol)

# 给定区间的解
sol = sp.solveset(x ** 2 - 1, x, sp.Interval(0, 100))
print(sol)

# 序列
from sympy.abc import x

s = sp.sequence(x, (x, 1, 10))
print(s)
sp.pprint(s)
print(list(s))

print(s.length)
print(s.start)
print(sp.summation(s.formula, (x, s.start, s.stop)))

from sympy.abc import x

l1 = sp.limit(1 / x, x, sp.oo)
print(l1)

l2 = sp.limit(1 / x, x, 0)
print(l2)

# 矩阵运算
M = sp.Matrix([[1, 2], [3, 4], [0, 3]])
print(M)
sp.pprint(M)

N = sp.Matrix([2, 2])

print("---------------------------")
print("M * N")
print("---------------------------")

sp.pprint(M * N)

# 画图
from sympy.abc import x
from sympy.plotting import plot

plot(x ** 2)
