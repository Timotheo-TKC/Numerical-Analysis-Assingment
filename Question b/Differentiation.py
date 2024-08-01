import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

# Define a function
def f(x):
    return x**3 + 2*x**2 + x + 1

# Calculate the derivative at a point
x = 1
dfdx = derivative(f, x, dx=1e-6)
print(f"The derivative of f at x = {x} is {dfdx}")

# Plot the function and its derivative
x_vals = np.linspace(-3, 3, 400)
f_vals = f(x_vals)
dfdx_vals = derivative(f, x_vals, dx=1e-6)

plt.plot(x_vals, f_vals, label='f(x)')
plt.plot(x_vals, dfdx_vals, label="f'(x)")
plt.legend()
plt.show()
