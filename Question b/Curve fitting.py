import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define a model function
def model(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate some data
x_data = np.linspace(0, 4, 50)
y_data = model(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=x_data.size)

# Fit the model to the data
popt, pcov = curve_fit(model, x_data, y_data)
print(f"Fitted parameters: {popt}")

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *popt), label='Fitted curve')
plt.legend()
plt.show()

