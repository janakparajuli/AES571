import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load DSD data
nd_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\nd.txt"
npol_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\npol.txt"

# Define bin centers and bin width
bin_centers = np.arange(0.3, 9.9, 0.2)
bin_width = 0.2  # mm

# Constants for rain rate
alpha = 3.78
beta = 0.67
PI = 3.1415
rain_coeff = (3.6e-3 * PI * alpha) / 6

# Read nd.txt
nd_data = pd.read_csv(nd_file, delim_whitespace=True, header=None)
nd_data.columns = ["Time"] + list(bin_centers)
nd_data["Time"] = pd.to_datetime(nd_data["Time"], format="%H:%M:%S")

# Compute dBZ and rain rate
z_values = []
rain_rates = []

for _, row in nd_data.iterrows():
    N_D = row[1:].values
    z = np.sum(N_D * (bin_centers**6) * bin_width)
    r = rain_coeff * np.sum(N_D * (bin_centers**beta) * bin_width)
    z_values.append(z)
    rain_rates.append(r)

nd_data["dBZ_2DVD"] = 10 * np.log10(z_values)
nd_data["RainRate"] = rain_rates  # in mm/hr

# Load npol data
npol_data = pd.read_csv(npol_file, delim_whitespace=True, header=None, names=["Time", "dBZ_NPOL"])
npol_data["Time"] = pd.to_datetime(npol_data["Time"], format="%H:%M:%S")

# Merge on time
merged = pd.merge(nd_data[["Time", "dBZ_2DVD", "RainRate"]], npol_data, on="Time", how="inner")

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Left Y-axis: Rain Rate
ax1.set_xlabel('Time', fontsize=12, font="Century")
ax1.set_ylabel('Rain Rate (mm/hr)', color='blue', fontsize=12, font="Century")
ax1.plot(merged["Time"], merged["RainRate"], color='blue', linewidth=1.5, label='Rain Rate', marker='o')
ax1.tick_params(axis='y', labelcolor='blue')

# Right Y-axis: Reflectivity (dBZ)
ax2 = ax1.twinx()
ax2.set_ylabel('Reflectivity (dBZ)', color='red', fontsize=12, font="Century")
ax2.plot(merged["Time"], merged["dBZ_2DVD"], color='red', linestyle='--', linewidth=1.5, label='2DVD Reflectivity', marker='s')
ax2.plot(merged["Time"], merged["dBZ_NPOL"], color='green', linestyle='-.', linewidth=1.5, label='NPOL Reflectivity', marker='^')
ax2.tick_params(axis='y', labelcolor='red')

# Format time axis
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

# Font settings
for tick in ax1.get_xticklabels() + ax1.get_yticklabels() + ax2.get_yticklabels():
    tick.set_fontname("Century")

# Transparent spines
for spine in ax1.spines.values():
    spine.set_alpha(0.0)
for spine in ax2.spines.values():
    spine.set_alpha(0.0)

# Title and Grid
plt.title('Rain Rate and Reflectivity from 2DVD and NPOL', fontdict={'fontname': 'Century', 'size': 14})
ax1.grid(True, linestyle='--', alpha=0.3)

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='upper right')

# Save and show
plt.tight_layout()
plt.savefig("rainrate_reflectivity_2dvd_npol.png")
plt.show()
