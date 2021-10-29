from NumericalMethod import *


class ImprovedEuler(NumericalMethod):
    def __init__(self, x, y, max_x, n):
        super().__init__(x, y, max_x, n)
        self.generate_y()
        self.lte_iem()
        self.gte_iem()

    def y_improved_euler(self, x, y):
        k1 = Function.y_prime(x, y)
        k2 = Function.y_prime(x + self.step, y + self.step * k1)
        return y + self.step * (k1 + k2) / 2.

    def generate_y(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i - 1]
            y = self.array_y[i - 1]
            self.array_y.append(self.y_improved_euler(x, y))

    def lte_iem(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i - 1]
            xe = self.array_x[i]
            super().lte(xe, self.y_improved_euler(x, Function.y_exact(x, self.c)))

    def gte_iem(self):
        for i in range(len(self.array_x)):
            x = self.array_x[i]
            y = self.array_y[i]
            super().gte(x, y)
