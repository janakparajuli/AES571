import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load DSD data
nd_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\nd.txt"
# npol_file = r"E:\UAH_Classes\AES_571\Assignments\Assignment_III\npol.txt"

# Define bin centers and bin width
bin_centers = np.arange(0.3, 9.9, 0.2)
bin_width = 0.2  # mm

# Define constants for rain rate
alpha = 3.78
beta = 0.67
PI = np.pi
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
    r = rain_coeff * np.sum(N_D * (bin_centers**beta) * bin_width)
    rain_rates.append(r)

# Add new columns
nd_data["RainRate"] = rain_rates  # in mm/hr

# Plotting rate
fig, ax1 = plt.subplots(figsize=(10, 6))

# Left Y-axis: Rain Rate
ax1.set_xlabel('Time', fontsize=12, font="Century")
ax1.set_ylabel('Rain Rate (mm/hr)', color='black', fontsize=12, font="Century")
ax1.plot(nd_data["Time"], nd_data["RainRate"], color='blue', linewidth=1.5, label='Rain Rate')
ax1.tick_params(axis='y', labelcolor='black')

# Format time axis
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)

# Font settings
for tick in ax1.get_xticklabels() + ax1.get_yticklabels(): # + ax2.get_yticklabels():
    tick.set_fontname("Century")

# Transparent spines
for spine in ax1.spines.values():
    spine.set_alpha(0.0)

# Title and Grid
plt.title('Rain Rate (mm/hr) calculated from 2DVD disdrometer data', fontdict={'fontname': 'Century', 'size': 14})
ax1.grid(True, linestyle='--', alpha=0.3)

# Save fig and show
plt.tight_layout()
plt.savefig("rainrate_reflectivity_2dvd_npol.png")
plt.show()
