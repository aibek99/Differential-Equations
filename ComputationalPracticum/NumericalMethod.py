from Function import *


# Class NumericalMethod inherits Class Grid,
# and computes LTE, GTE and stores them in corresponding lists
class NumericalMethod(Grid):
    def __init__(self, x, y, max_x, n):
        super().__init__(x, y, max_x, n)
        self.lte = [0]
        self.gte = []

    def lte(self, xe, y_method_at):
        self.lte.append(abs(Function.y_exact(xe, self.c) - y_method_at))

    def gte(self, x, y_method):
        self.gte.append(abs(Function.y_exact(x, self.c) - y_method))
