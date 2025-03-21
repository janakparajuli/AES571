import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.dates as mdates

# Load CSV containing RainRate and Reflectivity (z)
path = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\rainrate_reflectivity_2dvd.csv"
df = pd.read_csv(path)

# Filter valid data
df = df[(df["RainRate (mm/hr)"] > 0) & (df["Reflectivity"] > 0)]
rain_rate = df["RainRate (mm/hr)"]
z_linear = df["Reflectivity"]

# Define the power-law function
def power_law(R, a, b):
    return a * (R ** b)

# Set initial parameter guesses and bounds
initial_guess = [50, .5]  # Initial guesses for a and b
bounds = ([50, 0.5], [2000, 5])  # Lower and upper bounds for a and b

# Fit the power-law function using curve_fit with bounds
params, params_covariance = curve_fit(power_law, rain_rate, z_linear, p0=initial_guess, bounds=bounds)

# Extract fitted parameters
a, b = params

# Print the equation
print(f"Fitted Power-Law: z = {a:.2f} * R^{b:.2f}")

# Generate fitted curve
R_fit = np.linspace(min(rain_rate), max(rain_rate), 100)
z_fit = power_law(R_fit, a, b)

# Plot rain rate and reflectivity
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(rain_rate, z_linear, label="Observed Data", alpha=0.6, c='blue')
ax.plot(R_fit, z_fit, color='red', linewidth=2, label=f'Fit: z = {a:.2f} * R^{b:.2f}')

# Set axes scales
ax.set_xscale('linear')  # Rain rate on a linear scale
ax.set_yscale('log')  # Reflectivity on a logarithmic scale

# Labeling axes with Century font
ax.set_xlabel("Rain Rate R (mm/hr)", fontsize=12, fontname="Century")
ax.set_ylabel("Reflectivity z $(mm^6 m^{-3})$", fontsize=12, fontname="Century")

# Setting spines to be transparent
for spine in ax.spines.values():
    spine.set_alpha(0.2)

# Adding grid, title, legend
ax.grid(True, which='both', linestyle='--', alpha=0.3)
ax.set_title("Power-Law Relationship between z and R: z = a * R^b", fontsize=14, fontname="Century")
ax.legend()

# Tight layout for clean tight fit
plt.tight_layout()

# Save and show plot
plt.savefig("rainrate_reflectivity_2dvd.png")
plt.show()
