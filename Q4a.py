# !pip install ace_tools --quiet
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load DSD data in nd.txt
nd_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\nd.txt"

# Define bin centers from 0.3 mm to 9.7 mm increasing by 0.2 mm
bin_centers = np.arange(0.3, 9.9, 0.2)
bin_width = 0.2  # Bin width in mm

# Read nd.txt into a DataFrame
nd_data = pd.read_csv(nd_file, delim_whitespace=True, header=None)
nd_data.columns = ["Time"] + list(bin_centers)

# Convert time to datetime format
nd_data["Time"] = pd.to_datetime(nd_data["Time"], format="%H:%M:%S")

# Compute radar reflectivity factor z for each row
z = []
for index, row in nd_data.iterrows():
    N_D = row[1:].values  # Drop other values
    # Assuming given N_D are in m^-3 mm^-1
    z_values = np.sum(N_D * (bin_centers**6) * bin_width)  # Radar Reflectivity Factor
    z.append(z_values)

nd_data["Reflectivity"] = z
# Convert z to dBZ
nd_data["dBZ"] = 10 * np.log10(np.array(z))
# Check the range of dBZ values from the summary of data
# print(nd_data.describe())   # range: 26.850374, 51.273081 --> within range

# Plot z and dBZ
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Radar Reflectivity factor (z) on the left y-axis
ax1.set_xlabel('Time', fontsize=12)
ax1.set_ylabel('Radar Reflectivity factor, z ($mm^6 m^{-3}$)', color='blue', fontsize=12, font ="Century")
ax1.plot(nd_data["Time"], nd_data["Reflectivity"], color='blue', linewidth=2, label='Reflectivity (Z)')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis and plot dBZ on the right
ax2 = ax1.twinx()
ax2.set_ylabel('Radar Reflectivity factor, Z (dBZ)', color='red', fontsize=12)
ax2.plot(nd_data["Time"], nd_data["dBZ"], color='red', linestyle='--', linewidth=2, label='Reflectivity (dBZ)')
ax2.tick_params(axis='y', labelcolor='red')

# Title and Grid
plt.title('Radar Reflectivity Factors: z and Z vs. Time', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.7)

plt.savefig('radar_reflectivity_factors.png')
plt.show()

