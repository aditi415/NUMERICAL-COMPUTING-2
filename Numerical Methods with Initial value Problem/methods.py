
def f(x, y):
    """Define the differential equation dy/dx = f(x, y)."""
    return x + y 


def euler(x0, y0, h, n):
    x, y = x0, y0
    print("\n--- Euler Method ---")
    print("Step\tX\tY")
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        print(f"{i+1}\t{x:.4f}\t{y:.6f}")
    return y


def modified_euler(x0, y0, h, n):
    x, y = x0, y0
    print("\n--- Modified Euler Method ---")
    print("Step\tX\tY")
    for i in range(n):
        k1 = f(x, y)
        y_predict = y + h * k1
        k2 = f(x + h, y_predict)
        y = y + (h / 2) * (k1 + k2)
        x = x + h
        print(f"{i+1}\t{x:.4f}\t{y:.6f}")
    return y


def runge_kutta_4(x0, y0, h, n):
    x, y = x0, y0
    print("\n--- Runge-Kutta 4th Order Method ---")
    print("Step\tX\tY")
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + (h / 2) * k1)
        k3 = f(x + h / 2, y + (h / 2) * k2)
        k4 = f(x + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        print(f"{i+1}\t{x:.4f}\t{y:.6f}")
    return y
    
if __name__ == "__main__":
    x0 = 0       
    y0 = 1       
    h = 0.1      
    x_end = 0.5  

    n = int((x_end - x0) / h)  

    euler_y = euler(x0, y0, h, n)
    mod_euler_y = modified_euler(x0, y0, h, n)
    rk4_y = runge_kutta_4(x0, y0, h, n)

    print("\nFinal Results:")
    print(f"Euler Method Result: y({x_end}) = {euler_y:.6f}")
    print(f"Modified Euler Method Result: y({x_end}) = {mod_euler_y:.6f}")
    print(f"Runge-Kutta 4th Order Result: y({x_end}) = {rk4_y:.6f}")

