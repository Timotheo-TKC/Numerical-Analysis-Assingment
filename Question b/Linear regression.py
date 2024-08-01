import numpy as np
import matplotlib.pyplot as plt
# Generate some data
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + 1 + np.random.normal(0, 0.1, x.size)

# Perform linear regression
p = np.polyfit(x, y, 1)
print(f"Slope: {p[0]}, Intercept: {p[1]}")

# Plot the data and the fitted line
plt.scatter(x, y, label='Data')
plt.plot(x, np.polyval(p, x), label='Fitted line')
plt.legend()
plt.show()
