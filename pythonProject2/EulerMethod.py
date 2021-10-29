from NumericalMethod import *


class Euler(NumericalMethod):
    def __init__(self, x, y, max_n, n):
        super().__init__(x, y, max_n, n)
        self.generate_y()
        self.lte_em()
        self.gte_em()

    def y_euler(self, x, y):
        return y + Function.y_prime(x, y) * self.step

    def generate_y(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i - 1]
            y = self.array_y[i - 1]
            self.array_y.append(self.y_euler(x, y))

    def lte_em(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i - 1]
            xe = self.array_x[i]
            super().lte(xe, self.y_euler(x, Function.y_exact(x, self.c)))

    def gte_em(self):
        for i in range(len(self.array_x)):
            x = self.array_x[i]
            y = self.array_y[i]
            super().gte(x, y)
