# Class for exception
class ArgumentError(Exception):
    pass

# Define function f(x)
def f(x):

    return x*x*x+3*x-5
  
# Prints root of f(x) with error
def bisection(a,b,func):
    c = a

    while ((b-a) >= 0.001):
 
        # Find the middle point
        c = (a+b)/2
  
        # Check if this point is root
        if (func(c) == 0.0):
            break
  
        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
             
    return print(c)

try:
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
except:
    print("The input was not a valid number.")


if f(a) * f(b) > 0:
    raise ArgumentError("Invalid input")


bisection(a, b, f) 