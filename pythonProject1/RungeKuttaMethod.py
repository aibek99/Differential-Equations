from NumericalMethod import *


class RungeKutta(NumericalMethod):
    def __init__(self, x, y, max_x, n):
        super().__init__(x, y, max_x, n)
        self.generate_y()
        self.lte_rkm()
        self.gte_rkm()

    def y_runge_kutta(self, x, y):
        k1 = Function.y_prime(x, y)
        k2 = Function.y_prime(x + self.step / 2., y + k1 * self.step / 2.)
        k3 = Function.y_prime(x + self.step / 2., y + k2 * self.step / 2.)
        k4 = Function.y_prime(x + self.step, y + k3 * self.step)
        return y + self.step * (k1 + 2 * k2 + 2 * k3 + k4) / 6.

    def generate_y(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i - 1]
            y = self.array_y[i - 1]
            self.array_y.append(self.y_runge_kutta(x, y))

    def lte_rkm(self):
        for i in range(1, len(self.array_x)):
            x = self.array_x[i - 1]
            xe = self.array_x[i]
            super().lte(xe, self.y_runge_kutta(x, Function.y_exact(x, self.c)))

    def gte_rkm(self):
        for i in range(len(self.array_x)):
            x = self.array_x[i]
            y = self.array_y[i]
            super().gte(x, y)
