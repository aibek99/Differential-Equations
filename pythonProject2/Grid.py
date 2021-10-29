class Grid:
    def __init__(self, x, y, max_x, n):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.n = n
        self.step = (max_x - x) / n
        self.c = (y ** (1./3.)) - x
        self.array_x = [x]
        self.array_y = [y]
        self.generate_x()

    def get_x(self, i):
        return self.array_x[i]

    def get_y(self, i):
        return self.array_y[i]

    def get_max_x(self):
        return self.max_x

    def get_n(self):
        return self.n

    def get_step(self):
        return self.step

    def get_c(self):
        return self.c

    def generate_x(self):
        for i in range(self.n):
            self.array_x.append(self.get_x(i) + self.step)
