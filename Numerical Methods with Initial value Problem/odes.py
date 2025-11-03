import numpy as np
import matplotlib.pyplot as plt

class NumericalMethods:
    def __init__(self, func=None):
        self.func = func
    def euler(self, x0, y0, h, x_end):
        """Euler Method for solving dy/dx = f(x, y)."""
        n = int((x_end - x0) / h)
        x_values = [x0]
        y_values = [y0]
        x, y = x0, y0

        for _ in range(n):
            y = y + h * self.func(x, y)
            x = x + h
            x_values.append(x)
            y_values.append(y)

        return np.array(x_values), np.array(y_values)

    def modified_euler(self, x0, y0, h, x_end):
        n = int((x_end - x0) / h)
        x_values = [x0]
        y_values = [y0]
        x, y = x0, y0

        for _ in range(n):
            k1 = self.func(x, y)
            y_predict = y + h * k1
            k2 = self.func(x + h, y_predict)
            y = y + (h / 2) * (k1 + k2)
            x = x + h
            x_values.append(x)
            y_values.append(y)

        return np.array(x_values), np.array(y_values)
        
    def runge_kutta_4(self, x0, y0, h, x_end):
        n = int((x_end - x0) / h)
        x_values = [x0]
        y_values = [y0]
        x, y = x0, y0

        for _ in range(n):
            k1 = self.func(x, y)
            k2 = self.func(x + h/2, y + (h/2) * k1)
            k3 = self.func(x + h/2, y + (h/2) * k2)
            k4 = self.func(x + h, y + h * k3)
            y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
            x = x + h
            x_values.append(x)
            y_values.append(y)

        return np.array(x_values), np.array(y_values)


    def plot_ode_results(self, x_euler, y_euler, x_mod, y_mod, x_rk4, y_rk4):
        plt.figure(figsize=(8, 5))
        plt.plot(x_euler, y_euler, 'r--', label='Euler Method')
        plt.plot(x_mod, y_mod, 'b-.', label='Modified Euler')
        plt.plot(x_rk4, y_rk4, 'g-', label='Runge-Kutta 4th Order')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('ODE Solution Comparison')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def power_method_from_file(self, filename, max_iter=100, tol=1e-6):
        A = np.loadtxt(filename, dtype=float)
        n = A.shape[0]
        x = np.ones(n)
        lambda_old = 0.0

        print("\nMatrix Read from File:\n", A)
        print("\n--- Power Method Iterations ---")
        print("Iter\tEigenvalue\tEigenvector")

        for i in range(max_iter):
            y = np.dot(A, x)
            x = y / np.linalg.norm(y)
            lambda_new = np.dot(x, np.dot(A, x))
            print(f"{i+1}\t{lambda_new:.6f}\t{x}")
            if abs(lambda_new - lambda_old) < tol:
                print("\nConverged!")
                break
            lambda_old = lambda_new
        return lambda_new, x

if __name__ == "__main__":

    def f(x, y):
        return x**2 + y

    nm = NumericalMethods(func=f)

    x0 = 0
    y0 = 1
    h = 0.1
    x_end = 0.5

    x_euler, y_euler = nm.euler(x0, y0, h, x_end)
    x_mod, y_mod = nm.modified_euler(x0, y0, h, x_end)
    x_rk4, y_rk4 = nm.runge_kutta_4(x0, y0, h, x_end)

    nm.plot_ode_results(x_euler, y_euler, x_mod, y_mod, x_rk4, y_rk4)

    eigenvalue, eigenvector = nm.power_method_from_file("matrix.txt")
    print("\nDominant Eigenvalue:", round(eigenvalue, 6))
    print("Corresponding Eigenvector:", eigenvector)

