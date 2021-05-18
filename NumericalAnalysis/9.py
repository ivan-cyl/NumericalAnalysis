from sympy import *
import random

x = symbols("x")

func = x**3+2*x**2+10*x-20
ffunc = diff(func, x)

begin = 1
end = 2

MAXSTEP = 100

step_count = 0

x0 = random.uniform(begin, end)
temp = func.subs(x, x0)

while step_count < MAXSTEP and abs(temp) > 1e-10:
    x0 = x0 - (temp / (ffunc.subs(x, x0)))
    temp = func.subs(x, x0)
    step_count += 1
print(x0)
print(step_count)
