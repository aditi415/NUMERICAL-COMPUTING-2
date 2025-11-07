import math

class NumericalIntegration:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def f(self, x):
        return x**2   
        
    def exact_integral(self):
        return (self.b**3 - self.a**3) / 3

    def trapezoidal(self):
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            s += 2 * self.f(self.a + i * h)
        result = (h / 2) * s
        return result

    def simpson_one_third(self):
        if self.n % 2 != 0:
            print("n must be even for Simpson’s 1/3 rule.")
            return None
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            s += 4 * self.f(x) if i % 2 else 2 * self.f(x)
        result = (h / 3) * s
        return result

    def simpson_three_eighth(self):
        if self.n % 3 != 0:
            print("n must be multiple of 3 for Simpson’s 3/8 rule.")
            return None
        h = (self.b - self.a) / self.n
        s = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            x = self.a + i * h
            s += 3 * self.f(x) if i % 3 else 2 * self.f(x)
        result = (3 * h / 8) * s
        return result

    def error_analysis(self, numerical_value):
        exact = self.exact_integral()
        abs_error = abs(exact - numerical_value)
        percent_error = (abs_error / exact) * 100
        return abs_error, percent_error


if __name__ == "__main__":
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))
    n = int(input("Enter number of intervals n: "))

    ni = NumericalIntegration(a, b, n)

    print("\nNumerical Integration Results")
    exact_value = ni.exact_integral()
    print(f"Exact Integral (Analytical) = {exact_value:.6f}\n")

    trap = ni.trapezoidal()
    err_t, pct_t = ni.error_analysis(trap)
    print(f"Trapezoidal Rule = {trap:.6f}")
    print(f"Absolute Error = {err_t:.6e}")
    print(f"Percentage Error = {pct_t:.6f}%\n")

    simp13 = ni.simpson_one_third()
    if simp13 is not None:
        err_s13, pct_s13 = ni.error_analysis(simp13)
        print(f"Simpson’s 1/3 Rule = {simp13:.6f}")
        print(f"Absolute Error = {err_s13:.6e}")
        print(f"Percentage Error = {pct_s13:.6f}%\n")

    simp38 = ni.simpson_three_eighth()
    if simp38 is not None:
        err_s38, pct_s38 = ni.error_analysis(simp38)
        print(f"Simpson’s 3/8 Rule = {simp38:.6f}")
        print(f"Absolute Error = {err_s38:.6e}")
        print(f"Percentage Error = {pct_s38:.6f}%\n")

