import numpy as np

def forward_difference(x, y, value):
    n = len(x)
    h = x[1] - x[0]   
    
    diff = np.zeros((n, n))
    for i in range(n):
        diff[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

    print("\nForward Difference Table:")
    for i in range(n):
        print(diff[i][:n-i])
    

    u = (value - x[0]) / h
    result = y[0]
    term = 1
    for j in range(1, n):
        term *= (u - (j-1)) / j
        result += term * diff[0][j]

    return result



def backward_difference(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    diff = np.zeros((n, n))
    for i in range(n):
        diff[i][0] = y[i]


    for j in range(1, n):
        for i in range(j, n):
            diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

    print("\nBackward Difference Table:")
    for i in range(n):
        print(diff[i][:i+1])

    u = (value - x[-1]) / h
    result = y[-1]
    term = 1
    for j in range(1, n):
        term *= (u + (j-1)) / j
        result += term * diff[-1][j]

    return result


if __name__ =="__main__" :
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

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    print("\n--- Results ---")
    print("Forward Difference Result:", forward_difference(x, y, value))
    print("Backward Difference Result:", backward_difference(x, y, value))

