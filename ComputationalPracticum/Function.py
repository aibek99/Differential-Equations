from Grid import *

# Class Function inherits Class Grid,
# and has two important functions such as y_exact, y_prime and they are static


class Function(Grid):
    def __init__(self, x, y, max_x, n):
        super().__init__(x, y, max_x, n)

    @staticmethod
    def y_exact(x, c):
        return (x + c) ** 3

    @staticmethod
    def y_prime(x, y):
        return 3 * (y ** (2./3.))
