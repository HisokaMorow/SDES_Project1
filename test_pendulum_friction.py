from pendulum_friction import pendulum_diff as pd
from scipy.integrate import odeint

import matplotlib.pyplot as plt
import math as m
import numpy as np
import unittest

class TestProject1(unittest.TestCase):

  """
  test_pendulum_diff : Checks the validity of the differential equation.
  test_pendulum_diff_solution_1 : checks the solution at (0,0) initial condition.
  test_pendulum_diff_solution_2 : checks the solution at (pi,0) initial condition. 
  """
  def test_pendulum_diff(self):
    sol = pd([0,0],10)
    self.assertAlmostEqual(sol[0],0.0)
    self.assertAlmostEqual(sol[1],0.0)

  def test_pendulum_diff_solution_1(self):
    t = np.linspace(0, 1, 11)
    sol = odeint(pd,[0,0],t)
    for i in range(11):
      self.assertAlmostEqual(sol[i,0],0.0)
      self.assertAlmostEqual(sol[i,1],0.0)

  def test_pendulum_diff_solution_2(self):
    t = np.linspace(0, 1, 11)
    sol = odeint(pd,[m.pi,0],t)
    for i in range(11):
      self.assertAlmostEqual(sol[i,0],m.pi)
      self.assertAlmostEqual(sol[i,1],0.0)

if __name__ == '__main__':
  unittest.main()
