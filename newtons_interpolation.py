import numpy as np

class DifferenceInterpolation:
    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.n = len(x)
        self.h = self.x[1] - self.x[0]   

    def forward_difference(self, value):
        n = self.n
        diff = np.zeros((n, n))
        diff[:, 0] = self.y

        for j in range(1, n):
            for i in range(n - j):
                diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

        print("\nForward Difference Table:")
        for i in range(n):
            print(diff[i][:n-i])


        u = (value - self.x[0]) / self.h
        result = self.y[0]
        term = 1
        for j in range(1, n):
            term *= (u - (j-1)) / j
            result += term * diff[0][j]

        return result


    def backward_difference(self, value):
        n = self.n
        diff = np.zeros((n, n))
        diff[:, 0] = self.y

        for j in range(1, n):
            for i in range(j, n):
                diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

        print("\nBackward Difference Table:")
        for i in range(n):
            print(diff[i][:i+1])

    
        u = (value - self.x[-1]) / self.h
        result = self.y[-1]
        term = 1
        for j in range(1, n):
            term *= (u + (j-1)) / j
            result += term * diff[-1][j]

        return result



if __name__ == "__main__":
    n = int(input("Enter number of data points: "))
    x = []
    y = []

    print("\nEnter data points (x and y):")
    for i in range(n):
        xi = float(input(f"x[{i}]: "))
        yi = float(input(f"y[{i}]: "))
        x.append(xi)
        y.append(yi)

    value = float(input("\nEnter the value to interpolate at: "))

    interp = DifferenceInterpolation(x, y)

    print("\n--- Results ---")
    print("Forward Difference Result:", interp.forward_difference(value))
    print("Backward Difference Result:", interp.backward_difference(value))

