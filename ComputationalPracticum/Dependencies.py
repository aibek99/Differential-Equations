from EulerMethod import *
from ImprovedEulerMethod import *
from RungeKuttaMethod import *

# Class Dependencies uses all classes which are inherited Class NumericalMethod
# and stores dependencies list of GTE and LTE for each method


class Dependencies:
    def __init__(self, x0, y0, max_x, n, n0):
        self.legte = []
        self.ligte = []
        self.lrgte = []
        self.lelte = []
        self.lilte = []
        self.lrlte = []
        self.len = []

        for i in range(0, n - n0 + 1):
            euler = Euler(x0, y0, max_x, i + n0)
            improved = ImprovedEuler(x0, y0, max_x, i + n0)
            runge = RungeKutta(x0, y0, max_x, i + n0)
            self.len.append(i + n0)
            self.legte.append(max(euler.gte))
            self.ligte.append(max(improved.gte))
            self.lrgte.append(max(runge.gte))
            self.lelte.append(max(euler.lte))
            self.lilte.append(max(improved.lte))
            self.lrlte.append(max(runge.lte))
