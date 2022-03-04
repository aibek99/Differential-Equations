from Function import *


# Class Exact Solution inherits Grid, and generates list of y's


class ExactSolution(Grid):
    def __init__(self, x, y, max_x, n):
        super().__init__(x, y, max_x, n)
        self.generate_y()

    def y_exact(self, x):
        return Function.y_exact(x, self.c)

    def generate_y(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i]
            self.array_y.append(self.y_exact(x))
