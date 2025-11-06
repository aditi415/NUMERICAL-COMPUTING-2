import numpy as np

class Interpolation:
    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.n = len(x)

    # ----------------- Divided Difference ----------------
    def divided_difference(self, value):
        n = self.n
        x, y = self.x, self.y
        coef = np.zeros([n, n])
        coef[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

        result = coef[0][0]
        term = 1
        for j in range(1, n):
            term *= (value - x[j-1])
            result += coef[0][j] * term
        return result

    # ----------------- Forward Difference -----------------
    def forward_difference(self, value):
        n = self.n
        x, y = self.x, self.y
        h = x[1] - x[0]
        diff = np.zeros((n, n))
        diff[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

        u = (value - x[0]) / h
        result = y[0]
        term = 1
        for j in range(1, n):
            term *= (u - (j-1)) / j
            result += term * diff[0][j]
        return result

    # ----------------- Backward Difference -----------------
    def backward_difference(self, value):
        n = self.n
        x, y = self.x, self.y
        h = x[1] - x[0]
        diff = np.zeros((n, n))
        diff[:, 0] = y

        for j in range(1, n):
            for i in range(j, n):
                diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

        u = (value - x[-1]) / h
        result = y[-1]
        term = 1
        for j in range(1, n):
            term *= (u + (j-1)) / j
            result += term * diff[-1][j]
        return result

    # ----------------- Stirling’s Interpolation -----------------
    def stirling_interpolation(self, value):
        n = self.n
        x, y = self.x, self.y
        h = x[1] - x[0]
        mid = n // 2

        diff = np.zeros((n, n))
        diff[:, 0] = y
        for j in range(1, n):
            for i in range(n - j):
                diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

        u = (value - x[mid]) / h
        result = y[mid]
        term = 1
        fact = 1
        j = 1
        k = 1
        while j < n:
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

    # ----------------- Lagrange’s Interpolation -----------------
    def lagrange_interpolation(self, value):
        n = self.n
        x, y = self.x, self.y
        result = 0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if i != j:
                    term *= (value - x[j]) / (x[i] - x[j])
            result += term
        return result


# ----------------- Example Usage -----------------
if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [1, 2, 4, 8, 16]  # y = 2^x
    value = 2.5

    interp = Interpolation(x, y)

    print("Divided Difference:", interp.divided_difference(value))
    print("Forward Difference:", interp.forward_difference(value))
    print("Backward Difference:", interp.backward_difference(value))
    print("Stirling Interpolation:", interp.stirling_interpolation(value))
    print("Lagrange Interpolation:", interp.lagrange_interpolation(value))
