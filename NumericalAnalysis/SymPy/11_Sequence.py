from sympy import summation, sequence, pprint
from sympy.abc import x

# 序列是其中允许重复的对象的枚举集合。 序列可以是有限的或无限的。 元素的数量称为序列的长度。 与集合不同，同一元素可以在序列中的不同位置出现多次。 元素的顺序很重要

s = sequence(x, (x, 1, 10))
print(s)
pprint(s)
print(list(s))

print(s.length)

print(summation(s.formula, (x, s.start, s.stop)))
print(sum(list(s)))
