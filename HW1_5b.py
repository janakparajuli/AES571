###### Code goes here

import numpy as np
import matplotlib.pyplot as plt

# Define the function to calculate relative gain based on the given formula
def relative_gain(theta, theta_0):
    return - 40 * np.log(2) / np.log(10) * (theta / theta_0)**2

# Set the beamwidths and angular distances
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



# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Constants
# ln2 = np.log(2)
# ln10 = np.log(10)
# constant = -40 * ln2 / ln10
#
# # Function to compute G - G0
# def relative_gain(theta, theta_0):
#     return constant * (theta / theta_0)**2
#
# # Generate a plot for relative gain
# def plot_relative_gain():
#     theta_values = np.linspace(0, 2.5, 500)  # angular range for plotting
#     theta_0_1 = 1.0  # beamwidth 1 degree
#     theta_0_2 = 2.0  # beamwidth 2 degrees
#     gain_1 = relative_gain(theta_values, theta_0_1)
#     gain_2 = relative_gain(theta_values, theta_0_2)
#
#     plt.figure(figsize=(10, 6))
#     plt.plot(theta_values, gain_1, label='Beamwidth 1.0 degree')
#     plt.plot(theta_values, gain_2, label='Beamwidth 2.0 degrees')
#     plt.title('Relative Gain as a Function of Angular Distance')
#     plt.xlabel('Angular Distance (degrees)')
#     plt.ylabel('Relative Gain G - G0 (dB)')
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
# # Calculate and display relative gains at specific angular distances
# def calculate_specific_gains():
#     specific_theta = np.array([0.5, 1.0, 1.5, 2.0])
#     gain_at_specific_theta_1 = relative_gain(specific_theta, 1.0)
#     gain_at_specific_theta_2 = relative_gain(specific_theta, 2.0)
#
#     results_table = pd.DataFrame({
#         'Angular Distance (degrees)': specific_theta,
#         'Relative Gain (1.0 degree BW) (dB)': gain_at_specific_theta_1,
#         'Relative Gain (2.0 degree BW) (dB)': gain_at_specific_theta_2
#     })
#
#     print(results_table)
#
# # Main function to execute the plot and calculation functions
# if __name__ == "__main__":
#     plot_relative_gain()
#     calculate_specific_gains()
