from sympy import sqrt, pprint, Mul

x = sqrt(2)
y = sqrt(2)

pprint(Mul(x, y, evaluate=False))
# evaluate属性推迟对乘法表达式的求值

print('equals to ')
print(x * y)
