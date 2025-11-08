import math

def f(x):
    return x**2 

def trapezoidal(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return (h / 2) * s


def simpson_one_third(a, b, n):
    if n % 2 != 0:
        print("n must be even for Simpson’s 1/3 rule.")
        return None
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    return (h / 3) * s



def simpson_three_eighth(a, b, n):
    if n % 3 != 0:
        print("n must be multiple of 3 for Simpson’s 3/8 rule.")
        return None
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            s += 2 * f(x)
        else:
            s += 3 * f(x)
    return (3 * h / 8) * s



a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of intervals n: "))

print(f"\nTrapezoidal Rule = {trapezoidal(a, b, n):.6f}")

res1 = simpson_one_third(a, b, n)
if res1 is not None:
    print(f"Simpson’s 1/3 Rule = {res1:.6f}")

res2 = simpson_three_eighth(a, b, n)
if res2 is not None:
    print(f"Simpson’s 3/8 Rule = {res2:.6f}")

