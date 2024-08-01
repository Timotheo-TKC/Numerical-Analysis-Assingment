import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of a function f from a to b using the trapezoidal rule.
    
    Parameters:
    - f: The function to integrate.
    - a: The start of the integration interval.
    - b: The end of the integration interval.
    - n: The number of intervals (trapezoids).
    
    Returns:
    - The approximate integral value.
    """
    # Width of each trapezoid
    h = (b - a) / n
    
    # Compute the x values at the interval points
    x = np.linspace(a, b, n+1)
    
    # Compute the y values of the function at the interval points
    y = f(x)
    
    # Compute the area using the trapezoidal rule
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    
    return integral

# Define the function to integrate
def f(x):
    return x**2 + 3*x + 2

# Define integration limits and number of intervals
a = 0
b = 2
n = 10

# Compute the integral using the trapezoidal rule
integral = trapezoidal_rule(f, a, b, n)

print(f"The approximate integral of f(x) from {a} to {b} using {n} intervals is {integral:.4f}")
