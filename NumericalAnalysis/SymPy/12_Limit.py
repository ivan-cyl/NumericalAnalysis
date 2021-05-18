from sympy import sin, limit, oo
from sympy.abc import x

# 极限是函数（或序列）“接近”作为输入（或索引）“接近”某个值的值

l1 = limit(1 / x, x, oo)
print(l1)

l2 = limit(1 / x, x, 0)
print(l2)
