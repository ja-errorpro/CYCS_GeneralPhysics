# 3_D_2.py
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt

import numpy as np
from scipy.integrate import odeint
from math import *
import wx


g = 9.8
class DoublePendulum(object):
    def __init__(self,m1,m2,L1,L2):
        self.m1, self.m2 = m1, m2
        self.L1, self.L2 = L1, L2
        self.init_stat = np.array([0.0, 0.0, 0.0, 0.0])

    def equations(self,w,t):
        m1, m2, L1, L2 = self.m1, self.m2, self.L1, self.L2
        theta1, theta2, v1, v2 = w
        dth1 = v1
        dth2 = v2

        eq1a = (m1+m2)*L1*L1
        eq1b = m2*L1*L2*cos(theta1-theta2)
        eq1c = L1*(m2*L2*dth2*dth2*sin(theta1-theta2) + (m1+m2)*g*sin(theta1))

        eq2a = L1*m2*L2*cos(theta1-theta2)
        eq2b = L2*L2*m2
        eq2c = m2*L2*(-L1*dth1*dth1*sin(theta1-theta2) + g*sin(theta2))

        dv1, dv2 = np.linalg.solve([[eq1a, eq1b], [eq2a, eq2b]], [-eq1c, -eq2c])

        return np.array([dth1, dth2, dv1, dv2])

def double_pendulum_odeint(pendulum, l, r, step):
    t = np.arange(l,r,step)
    trk = odeint(pendulum.equations, pendulum.init_stat, t)
    theta1, theta2 = trk[:,0], trk[:,1]
    L1 = pendulum.L1
    L2 = pendulum.L2
    x1 = L1*np.sin(theta1)
    y1 = -L1*np.cos(theta1)
    x2 = x1 + L2*np.sin(theta2)
    y2 = y1 - L2*np.cos(theta2)
    pendulum.init_stat = trk[-1,:].copy()
    return [x1, y1, x2, y2]

fig = plt.figure(figsize=(6,6))

line1, = plt.plot([0,0],[0,0],"-o")
line2, = plt.plot([0,0],[0,0],"-o")
plt.axis("equal")
plt.xlim(-5,5)
plt.ylim(-5,5)

print('模擬雙擺運動(若直接按下Enter則使用預設值)：')

m1 = input('請輸入m1質量[1.0]：')
if m1 == '':
    m1 = 1.0
m2 = input('請輸入m2質量[1.0]：')
if m2 == '':
    m2 = 1.0
L1 = input('請輸入L1長度[1.0]：')
if L1 == '':
    L1 = 1.0
L2 = input('請輸入L2長度[1.0]：')
if L2 == '':
    L2 = 1.0

pendulum = DoublePendulum(m1, m2, L1, L2)
theta1 = input('請輸入初始theta1角度(徑度)[1.0]：')
if theta1 == '':
    theta1 = 1.0
theta2 = input('請輸入初始theta2角度(徑度)[1.0]：')
if theta2 == '':
    theta2 = 1.0
pendulum.init_stat[:2] = theta1, theta2

x1,y1,x2,y2 = double_pendulum_odeint(pendulum, 0, 30, 0.02)
plt.plot(x1,y1,label="m_1")
plt.plot(x2,y2,label="m_2")

plt.title("m1 = %s, m2 = %s, L1 = %s, L2 = %s, theta1 = %s, theta2 = %s" % (m1, m2, L1, L2, theta1, theta2))

idx = 0

def update_line(event):
    global x1,y1,x2,y2,idx
    if idx == len(x1):
        idx = 0
        x1, y1, x2, y2 = double_pendulum_odeint(pendulum, 0, 30, 0.02)
    line1.set_xdata([0,x1[idx]])
    line1.set_ydata([0,y1[idx]])
    line2.set_xdata([x1[idx],x2[idx]])
    line2.set_ydata([y1[idx],y2[idx]])
    fig.canvas.draw()
    idx += 1

id = wx.ID_ANY
actor = fig.canvas.manager.frame
actor.Bind(wx.EVT_TIMER, update_line, id=id)
timer = wx.Timer(actor, id)
timer.Start(1)

plt.legend()

plt.show()