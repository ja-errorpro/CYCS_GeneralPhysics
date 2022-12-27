import math
R = 6.4e6
T = 86400
g = 9.8
pi = math.pi
H = (g*(R**2)*(T**2)/(4*(pi**2)))**(1/3) - R
print(H, "m, or ", H/1000, "km")
