import numpy as np
from scipy.interpolate import UnivariateSpline

# Generate some data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Perform spline interpolation
spline = UnivariateSpline(x, y, s=0)

# Generate new x values and evaluate the spline
x_new = np.linspace(0, 10, 100)
y_new = spline(x_new)

# Plot the original data and the spline interpolation
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, label='Spline interpolation')
plt.legend()
plt.show()
