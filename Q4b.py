import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load DSD data in nd.txt
nd_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\nd.txt"
npol_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\npol.txt"

# Define bin centers and bin width
bin_centers = np.arange(0.3, 9.9, 0.2)
bin_width = 0.2  # mm

# Read nd.txt
nd_data = pd.read_csv(nd_file, delim_whitespace=True, header=None)
nd_data.columns = ["Time"] + list(bin_centers)
nd_data["Time"] = pd.to_datetime(nd_data["Time"], format="%H:%M:%S")

# Compute radar reflectivity factor z for each row
z_values = []
for _, row in nd_data.iterrows():
    N_D = row[1:].values
    # Assuming given N_D are in m^-3 mm^-1
    z = np.sum(N_D * (bin_centers**6) * bin_width) # Radar Reflectivity Factor
    z_values.append(z)

nd_data["dBZ_2DVD"] = 10 * np.log10(z_values)

# Read npol.txt
npol_data = pd.read_csv(npol_file, delim_whitespace=True, header=None, names=["Time", "dBZ_NPOL"])
npol_data["Time"] = pd.to_datetime(npol_data["Time"], format="%H:%M:%S")

# Merge data on time
merged = pd.merge(nd_data[["Time", "dBZ_2DVD"]], npol_data, on="Time", how="inner")

# Plotting dBZ comparison only
fig, ax = plt.subplots(figsize=(10, 6))

# Axis labels and plot
ax.set_xlabel('Time', fontsize=12, font="Century")
ax.set_ylabel('Reflectivity (dBZ)', fontsize=12, font="Century")
ax.plot(merged["Time"], merged["dBZ_2DVD"], color='blue', linewidth=1.5, label='2DVD Reflectivity (dBZ)', marker='o')
ax.plot(merged["Time"], merged["dBZ_NPOL"], color='red', linestyle='--', linewidth=1.5, label='NPOL Reflectivity (dBZ)', marker='s')

# Format time axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

# Font settings
for tick in ax.get_xticklabels():
    tick.set_fontname("Century")
for tick in ax.get_yticklabels():
    tick.set_fontname("Century")

# Set transparency of the borders (spines)
alpha_value = 0.0
for spine in ax.spines.values():
    spine.set_alpha(alpha_value)

# Title, legend, grid
plt.title('Comparison of Reflectivity, Z (dBZ) from 2DVD and NPOL', fontdict={'fontname': 'Century', 'size': 14})
ax.grid(True, linestyle='--', alpha=0.3)
ax.legend(fontsize=10)

# Save and show
plt.tight_layout()
plt.savefig('compare_2dvd_npol_dBZ.png')
plt.show()
