# 3_C_1.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

g = 9.8
l = 1
def diff(y, t):
    omega, theta = y
    return np.array([-(g/l)*np.sin(theta), omega])
t = np.linspace(0, 10, 1000)
theta_0 = 50 / 180 * np.pi
ret = odeint(diff, [0, theta_0 ], t)

plt.plot(t, ret[:, 0])
plt.plot(t, ret[:, 1])
plt.show()