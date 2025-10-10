class LagrangeInterpolation:
    def __init__(self, x_points, y_points):
        if len(x_points) != len(y_points):
            raise ValueError("x_points and y_points must be the same length")
        self.x_points = x_points
        self.y_points = y_points
        self.n = len(x_points)

    def interpolate(self, x):
        """Evaluate Lagrange interpolating polynomial at given x."""
        result = 0.0
        for i in range(self.n):
            term = self.y_points[i]
            for j in range(self.n):
                if i != j:
                    term *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])
            result += term
        return result


if __name__ == "__main__":
    n = int(input("Enter number of data points: "))

    x_points = []
    y_points = []

    print("Enter x and y values:")
    for i in range(n):
        x_val = float(input(f"x[{i}]: "))
        y_val = float(input(f"y[{i}]: "))
        x_points.append(x_val)
        y_points.append(y_val)

 
    lagrange = LagrangeInterpolation(x_points, y_points)

 
    q = int(input("Enter number of query points: "))
    for k in range(q):
        x = float(input(f"Enter value of x[{k}] for interpolation: "))
        result = lagrange.interpolate(x)
        print(f"Interpolated value at x = {x} is {result:.6f}")

