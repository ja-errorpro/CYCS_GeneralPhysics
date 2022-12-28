# 3_D_1.py
from sympy import *
from sympy import Derivative as D

var("x1 x2 y1 y2 L1 L2 m1 m2 dtheta1 dtheta2 ddtheta1 ddtheta2 t g tmp")

var("theta1 theta2", cls=Function)


sublist = [
    (D(theta1(t), t, t), ddtheta1),
    (D(theta1(t), t), dtheta1),
    (D(theta2(t), t, t), ddtheta2),
    (D(theta2(t), t), dtheta2),
    (theta1(t), theta1()),
    (theta2(t), theta2())
]

x1 = L1 * sin(theta1(t))
y1 = -L1 * cos(theta1(t))
x2 = x1 + L2 * sin(theta2(t))
y2 = y1 - L2 * cos(theta2(t))

vx1 = diff(x1, t)
vy1 = diff(y1, t)
vx2 = diff(x2, t)
vy2 = diff(y2, t)

L = m1/2 * (vx1**2 + vy1**2) + m2/2 * (vx2**2 + vy2**2) - m1 * g * y1 - m2 * g * y2

def lagrange(L, v):
    dv = D(v(t),t)
    a = L.subs(dv, tmp).diff(tmp).subs(tmp, dv)
    b = L.subs(dv, tmp)
    b = b.subs(v(t),v())
    b = b.diff(v())
    b = b.subs(v(), v(t))
    b = b.subs(tmp, dv)
    c = a.diff(t) - b
    c = c.subs(sublist)
    c = trigsimp(simplify(c))
    c = collect(c, [theta1(),theta2(),dtheta1,dtheta2,ddtheta1,ddtheta2])
    return c

eq1 = lagrange(L, theta1)
eq2 = lagrange(L, theta2)

print("eq1 = ", eq1)
print("eq2 = ", eq2)