import matplotlib.pyplot as plt
import math as m
import numpy as np
from scipy.integrate import odeint

"""
Some constant required to solve
the differential equation

g is acceleration due to gravity in m/sec^2
L is the length of the string holding the pendulum in metres
M is the mass of the pendulum in Kg
b is coefficient of friction
initial is a list containing initial condition

Format of initial is as follows
[initial_angular_position(in radians), initial_angular_velocity(in radian/sec)
"""

g = 9.81
L = 0.2 
M = 0.4
b = 0.3
initial = [10*2*m.pi/360, 0]

def pendulum_diff(initial,t):

  """
  This function returns the derivative
  of states theta (angular position)
  and omega (angular velocity)

  The input to function is the previous
  value of states theta and omega
  """
  theta = initial[0]
  omega = initial[1]
  result = [omega, -(g/L)*m.sin(theta) - (b/M)*omega]
  return result

def state_plot(pend_sol,t):

  """
  This function plots state theta and omega vs time in a figure.
  """
  plt.figure(1)
  plt.plot(t,pend_sol[:,0],'.-',label='$\Theta$(Angular position)',linewidth=1,markersize=1,markeredgewidth=1,color='r')
  plt.plot(t,pend_sol[:,1], 'D-',label='d$\Theta$/dt(Angular Velocity)',linewidth=2,markersize=1,markeredgewidth=1,color='b')
  plt.grid()
  plt.title("Plot of $\Theta$ and d$\Theta$/dt vs Time")
  plt.xlabel("Time",fontname='serif',fontsize=12)
  plt.xticks(range(0, 10)[::1], family='serif', fontsize=8)
  plt.ylabel("States",fontname='serif',fontsize=12)
  plt.yticks(family='serif', fontsize=12)
  plt.legend(prop={'family': 'serif', 'size': 12})
  plt.savefig("fig(1).png")


def inter_state_plot(pend_sol):

  """
  This function plots the graph of omega vs theta 
  """
  plt.figure(2)
  plt.grid()
  plt.plot(pend_sol[:,0],pend_sol[:,1], linewidth=2, label='Inter state Plot')
  plt.title('Inter state plot between d$\Theta$/dt and $\Theta$')
  plt.xlabel('$\Theta$(Angular position)', fontname='serif', fontsize=12)
  plt.ylabel('d$\Theta$/dt(Angular Velocity)', fontname='serif', fontsize=12)
  plt.savefig('fig(2).png') 
  

def main():
  t = np.linspace(0, 20, 5001)
  pend_sol = odeint(pendulum_diff,initial,t)
  state_plot(pend_sol,t)
  inter_state_plot(pend_sol)

main()
