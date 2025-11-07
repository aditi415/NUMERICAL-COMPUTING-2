import numpy as np

class Interpolation:
    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.n = len(x)

    def divided_difference(self, value):
        coef = np.zeros([self.n, self.n])
        coef[:, 0] = self.y

        for j in range(1, self.n):
            for i in range(self.n - j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (self.x[i+j] - self.x[i])

        result = coef[0][0]
        term = 1
        for j in range(1, self.n):
            term *= (value - self.x[j-1])
            result += coef[0][j] * term
        return result

    def forward_difference(self, value):
        h = self.x[1] - self.x[0]
        diff = np.zeros((self.n, self.n))
        diff[:, 0] = self.y

        for j in range(1, self.n):
            for i in range(self.n - j):
                diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

        u = (value - self.x[0]) / h
        result = self.y[0]
        term = 1
        for j in range(1, self.n):
            term *= (u - (j-1)) / j
            result += term * diff[0][j]
        return result

    def backward_difference(self, value):
        h = self.x[1] - self.x[0]
        diff = np.zeros((self.n, self.n))
        diff[:, 0] = self.y

        for j in range(1, self.n):
            for i in range(j, self.n):
                diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

        u = (value - self.x[-1]) / h
        result = self.y[-1]
        term = 1
        for j in range(1, self.n):
            term *= (u + (j-1)) / j
            result += term * diff[-1][j]
        return result

    def stirling_interpolation(self, value):
        h = self.x[1] - self.x[0]
        mid = self.n // 2

        diff = np.zeros((self.n, self.n))
        diff[:, 0] = self.y
        for j in range(1, self.n):
            for i in range(self.n - j):
                diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

        u = (value - self.x[mid]) / h
        result = self.y[mid]

        term = 1
        fact = 1
        j = 1
        k = 1
        while j < self.n:
            if j % 2 == 1:  # odd term
                term *= u**2 - (k-1)**2
                fact *= j * (j+1)
                result += term * (diff[mid-k][j] + diff[mid-k+1][j]) / (2*fact)
                k += 1
            else:  # even term
                term *= (u**2 - (k-1)**2)
                fact *= j
                result += term * diff[mid-k][j] / fact
            j += 1
        return result

    def lagrange_interpolation(self, value):
        result = 0
        for i in range(self.n):
            term = self.y[i]
            for j in range(self.n):
                if i != j:
                    term *= (value - self.x[j]) / (self.x[i] - self.x[j])
            result += term
        return result

if __name__ == "__main__":
    n = int(input("Enter number of data points: "))

    x = []
    y = []
    print("Enter x and y values:")
    for i in range(n):
        xi = float(input(f"x[{i}] = "))
        yi = float(input(f"y[{i}] = "))
        x.append(xi)
        y.append(yi)

    value = float(input("Enter the value of x for interpolation: "))

    interp = Interpolation(x, y)

    print("\n     Interpolation Results    ")
    print("Divided Difference:", interp.divided_difference(value))
    print("Forward Difference:", interp.forward_difference(value))
    print("Backward Difference:", interp.backward_difference(value))
    print("Stirling Interpolation:", interp.stirling_interpolation(value))
    print("Lagrange Interpolation:", interp.lagrange_interpolation(value))

