import numpy as np
from scipy.integrate import quad

# Define a function
def g(x):
    return np.sin(x)

# Calculate the integral from 0 to pi
integral, error = quad(g, 0, np.pi)
print(f"The integral of g from 0 to pi is {integral}")

