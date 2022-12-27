# 1_C.py
import math
R = 6.4e6
T = 86400
g = 9.8
pi = math.pi
H_B = (g*(R**2)*(T**2)/(4*(pi**2)))**(1/3) - R
H_C = 5e5
T_C = math.sqrt(((R+H_C)**3)/((R+H_B)**3)*(T**2))
print(T_C, "s")
