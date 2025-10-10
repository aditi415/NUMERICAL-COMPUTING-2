from integral_methods import Integral

func = input("Enter function f(x): ")
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter number of subintervals (n): "))

I = Integral(func, a, b, n)

print("\nResults:")
print(f"Trapezoidal Rule: {I.trapezoidal():.3f}")

if n % 2 == 0:
    print(f"Simpson's 1/3 Rule: {I.simpson_one_third():.3f}")
else:
    print("Simpson's 1/3 Rule: n must be even")

if n % 3 == 0:
    print(f"Simpson's 3/8 Rule : {I.simpson_three_eighth():.3f}")
else:
    print("Simpson's 3/8 Rule: n must be multiple of 3")























#-----from integral_methods import Integral

#if __name__ == "__main__":
    #func = input("Enter function f(x): ")
   # a = float(input("Enter lower limit (a): "))
  #  b = float(input("Enter upper limit (b): "))
 #   n = int(input("Enter number of intervals (n): "))

#ni = NumericalIntegration(func, a, b, n)

#print("\nResults:")
#print(f"Trapezoidal Rule: {ni.trapezoidal():.2f}")

#print(f"Simpsons 1/3rd Rule: {ni.simpson_one_third():.3f}")

#print(f"Simpsons 3/8th Rule: {ni.simpson_three_eight():.3f}")
