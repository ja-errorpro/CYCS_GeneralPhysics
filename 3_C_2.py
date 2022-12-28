# 3_C.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

theta_0 = np.linspace(0, np.pi, 100)
L = 1
g = 9.8
omega_0 = np.sqrt(g/L)
T_0 = 2*np.pi/omega_0
T = 4*np.sqrt(L/g)*special.ellipk(np.sin(theta_0/2))
plt.plot(theta_0, T/T_0)
plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$T/T_0$')
plt.show()