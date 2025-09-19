import numpy as np

class DividedDifference:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.table = self.build_table()

    def build_table(self):
        n = self.n
        table = []
        for i in range(n):
            row = [0]*n
            table.append(row)

        for i in range(n):
            table[i][0] = self.y[i]

        for j in range(1, n):
            for i in range(n-j):
                table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (self.x[i+j] - self.x[i])
        return table

    def coefficients(self):
        return [self.table[0][j] 
            for j in range(self.n)]

    def evaluate(self, value):
        coeffs = self.coefficients()
        result = coeffs[0]
        product = 1
        for i in range(1, self.n):
            product *= (value - self.x[i-1])
            result += coeffs[i] * product
        return result

    def show_table(self):
        for row in self.table:
            print(row)

if __name__ == "__main__":
    x = [-2,0,1,2]
    y = [1,1,4,17]

    dd = DividedDifference(x, y)
    dd.show_table()
    print("Coefficients:", dd.coefficients())
    print("P(3) =", dd.evaluate(3))

