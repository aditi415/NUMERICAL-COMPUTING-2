import numpy as np
import matplotlib.pyplot as plt

class NumericalMethods:
    def __init__(self, func=None):
        self.func = func
        
    def euler(self, x0, y0, h, x_end):
        n = int((x_end - x0) / h)
        x_vals = [x0]
        y_vals = [y0]

        for _ in range(n):
            y0 = y0 + h * self.func(x0, y0)
            x0 = x0 + h
            x_vals.append(x0)
            y_vals.append(y0)

        return np.array(x_vals), np.array(y_vals)

    def modified_euler(self, x0, y0, h, x_end):
        n = int((x_end - x0) / h)
        x_vals = [x0]
        y_vals = [y0]

        for _ in range(n):
            k1 = self.func(x0, y0)
            y_pred = y0 + h * k1
            k2 = self.func(x0 + h, y_pred)
            y0 = y0 + (h / 2) * (k1 + k2)
            x0 = x0 + h
            x_vals.append(x0)
            y_vals.append(y0)

        return np.array(x_vals), np.array(y_vals)

    def runge_kutta_4(self, x0, y0, h, x_end):
        n = int((x_end - x0) / h)
        x_vals = [x0]
        y_vals = [y0]

        for _ in range(n):
            k1 = self.func(x0, y0)
            k2 = self.func(x0 + h/2, y0 + (h/2) * k1)
            k3 = self.func(x0 + h/2, y0 + (h/2) * k2)
            k4 = self.func(x0 + h, y0 + h * k3)
            y0 = y0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
            x0 = x0 + h
            x_vals.append(x0)
            y_vals.append(y0)

        return np.array(x_vals), np.array(y_vals)
        
    def plot_results(self, x_euler, y_euler, x_mod, y_mod, x_rk4, y_rk4):
        plt.plot(x_euler, y_euler, 'r--', label='Euler')
        plt.plot(x_mod, y_mod, 'b-.', label='Modified Euler')
        plt.plot(x_rk4, y_rk4, 'g-', label='Runge-Kutta 4')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('ODE Solution Comparison')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def power_method_from_file(self, filename, max_iter=100, tol=1e-6):
        A = np.loadtxt(filename)
        n = A.shape[0]
        x = np.ones(n)
        lambda_old = 0.0

        print("\nMatrix from file:\n", A)
        print("\nIteration\tEigenvalue\tEigenvector")

        for i in range(max_iter):
            y = np.dot(A, x)
            x = y / np.linalg.norm(y)
            lambda_new = np.dot(x, np.dot(A, x))
            print(f"{i+1}\t\t{lambda_new:.6f}\t{x}")
            if abs(lambda_new - lambda_old) < tol:
                print("Converged!")
                break
            lambda_old = lambda_new

        return lambda_new, x
        
if __name__ == "__main__":
    def f(x, y):
        return x**2 + y

    nm = NumericalMethods(f)

    x0, y0, h, x_end = 0, 1, 0.1, 0.5

    x_euler, y_euler = nm.euler(x0, y0, h, x_end)
    x_mod, y_mod = nm.modified_euler(x0, y0, h, x_end)
    x_rk4, y_rk4 = nm.runge_kutta_4(x0, y0, h, x_end)

    nm.plot_results(x_euler, y_euler, x_mod, y_mod, x_rk4, y_rk4)

    eigenvalue, eigenvector = nm.power_method_from_file("matrix.txt")
    print("\nDominant Eigenvalue:", round(eigenvalue, 6))
    print("Corresponding Eigenvector:", eigenvector)

