import math

class NumericalIntegration:
    def __init__(self, func, a, b, n):
        self.func = func      # function to integrate
        self.a = a            # lower limit
        self.b = b            # upper limit
        self.n = n            # number of subintervals

    def f(self, x):
        return eval(self.func)

    def trapezoidal(self):
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            s += 2 * self.f(x)
        return (h / 2) * s

    def simpson_one_third(self):
        if self.n % 2 != 0:
            print("For Simpson's 1/3rd rule, n must be even.")
            return None

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
        if self.n % 3 != 0:
            print("For Simpson's 3/8th rule, n must be a multiple of 3.")
            return None

        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            if i % 3 == 0:
                s += 2 * self.f(x)
            else:
                s += 3 * self.f(x)
        return (3 * h / 8) * s


# ---- MAIN PROGRAM ----
print("Numerical Integration Methods")
print("Function should be written using 'x' (e.g. math.sin(x), x**2, math.exp(x))")

func = input("Enter function f(x): ")
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter number of subintervals (n): "))

ni = NumericalIntegration(func, a, b, n)

print("\nResults:")
print(f"Trapezoidal Rule: {ni.trapezoidal():.6f}")

s13 = ni.simpson_one_third()
if s13 is not None:
    print(f"Simpson's 1/3rd Rule: {s13:.6f}")

s38 = ni.simpson_three_eighth()
if s38 is not None:
    print(f"Simpson's 3/8th Rule: {s38:.6f}")

