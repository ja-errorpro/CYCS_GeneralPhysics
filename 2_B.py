import matplotlib.pyplot as plt
import numpy as np

T = 323
k = 1.38e-23
m_A = np.linspace(1,100,100) # 設 m_A = 1~100 kg
m_B = np.linspace(50,100,100) # 設 m_B = 50~100 kg
E_act = 3*k*T - (3*k*T * (m_A + 50 - 2 * (m_A * 50)**0.5) ) / ( 2 * (m_A + 50) ) # 計算 Activation Energy
plt.plot(m_A,E_act, label = 'm_A')
plt.plot(m_B,E_act, label = 'm_B')
plt.plot(m_A + m_B,E_act, label = 'm_A + m_B')
plt.legend()
plt.xlabel('m (kg)')
plt.ylabel('Activation Energy (J)')
plt.show()
