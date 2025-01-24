###### Code goes here

import numpy as np
import matplotlib.pyplot as plt

# Define the function to calculate relative gain based on the given formula
def relative_gain(theta, theta_0):
    # G0 = 0  # assuming maximum decibel gain G0 is 0 for simplification
    return - 40 * np.log(2) / np.log(10) * (theta / theta_0)**2

# Set the beamwidths and angular distances
beamwidths = [1.0, 2.0]
thetas = np.array([0.5, 1.0, 1.5, 2.0])  # degrees

# Calculate relative gains for each beamwidth
gains = {bw: relative_gain(thetas, bw) for bw in beamwidths}

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
for bw, gains in gains.items():
    ax.plot(thetas, gains, marker='o', label=f'Beamwidth {bw}°')

ax.set_xlabel('Angular Distance from the Center Axis (°)')
ax.set_ylabel('Relative Gain (dB)')
ax.set_title('Relative Gain vs. Angular Distance for Different Beamwidths')
plt.grid(True)
plt.legend()
plt.show()

