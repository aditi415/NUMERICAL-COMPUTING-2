import math

class Integral:
    def __init__(self, func, a, b, n):
        self.func = func      
        self.a = a            
        self.b = b            
        self.n = n            

    def f(self, x):
        return eval(self.func)

    def trapezoidal(self):
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            s += 2 * self.f(self.a + i * h)
        return (h / 2) * s

    def simpson_one_third(self):
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            if i % 2 == 0:
                s += 2 * self.f(x)
            else:
                s += 4 * self.f(x)
        return (h / 3) * s

    def simpson_three_eighth(self):
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            if i % 3 == 0:
                s += 2 * self.f(x)
            else:
                s += 3 * self.f(x)
        return (3 * h / 8) * s














#return eval(self.func, {"x": x, "math": math})

