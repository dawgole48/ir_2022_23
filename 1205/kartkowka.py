import math

def f(x):
    return (4 - (x * x))

x1 = -2
x2 = 2
P = 0
n = 1000
h = (x2 - x1) / n

for i in range(0, n):
    p1 = f(x1 + (i * h))
    p2 = f(x1 + (i + 1) * h)
    P += (p1 + p2) * h / 2
    
print(P)