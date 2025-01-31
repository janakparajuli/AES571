###### Code goes here

import numpy as np
import matplotlib.pyplot as plt

# Define the function to calculate relative gain based on the eqn 7a, slide 30, Ch 2
def relative_gain(theta, theta_0):
    return - (40 * np.log(2) / np.log(10)) * (theta / theta_0)**2

# Set beamwidths and angular distances
beamwidths = [1.0, 2.0]
thetas = np.array([0, 0.5, 1.0, 1.5, 2.0])  # degrees

# Calculate relative gains for each beamwidth
gains = {bw: relative_gain(thetas, bw) for bw in beamwidths}

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
for bw, gains in gains.items():
    ax.plot(thetas, gains, marker='o', label=f'Beamwidth {bw}°')

ax.set_xlabel('Angular Distance from the Center Axis (°)', font='Century Gothic', fontsize=12)
ax.set_ylabel('Relative Gain (dB)', font='Century Gothic', fontsize=12)
ax.set_title('Relative Gain as a function of Angular Distance for Different Beamwidths', font='Century Gothic', fontsize=14)
ax.set_ylim(-50,5)
ax.set_xlim(0,2.5)
plt.grid(True, alpha=0.25)
plt.legend()
plt.show()

