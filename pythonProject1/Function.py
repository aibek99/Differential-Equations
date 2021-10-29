from Grid import *


class Function(Grid):
    def __init__(self, x, y, max_x, n):
        super().__init__(x, y, max_x, n)

    @staticmethod
    def y_exact(x, c):
        return (x + c) ** 3

    @staticmethod
    def y_prime(x, y):
        return 3 * (y ** (2./3.))
