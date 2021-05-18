from sympy import pprint, Symbol, exp, sqrt
from sympy import init_printing

# pprint()用于在控制台上漂亮地打印输出。 LaTeX 可以达到最佳效果

init_printing(use_unicode=True)
# 对于某些字符，我们需要启用 unicode 支持

x = Symbol('x')

a = sqrt(2)
pprint(a)
print(a)

print("------------------------")

c = (exp(x) ** 2) / 2
pprint(c)
print(c)
