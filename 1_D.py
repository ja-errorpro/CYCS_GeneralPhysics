# 1_D.py
import math
R = 6400
pi = math.pi
H_B = 35940
H_C = 500
S_B = 2*pi*(R**2)*(1-R/(R+H_B))
S_C = 2*pi*(R**2)*(1-R/(R+H_C))
print("S_B: ", S_B, "km^2")
print("S_C: ", S_C, "km^2")
