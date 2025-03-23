import numpy as np
import matplotlib.pyplot as plt

# Define Radar Range Equation Parameters
MDS = -110   # dBm
C3 = 66.6    # dB, Radar Constant
L = -1       # dB, Radar Loss
r = np.linspace(1, 150, 150)  # Range from 1 to 150 km
# print(r)

# Calculate Mean Detectable Reflectivity (MDR)
MDR = C3 + MDS + 20 * np.log10(r) - L

# Plot MDR
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(r, MDR, color='red', linewidth=2)

ax.set_title('CHILL Radar: Minimum Detectable Reflectivity vs. Range (L = -1 dB)', font='Century', fontsize=14)
ax.set_xlabel('Slant Range (km)', font='Century', fontsize=12)
ax.set_ylabel('MDR (dBZe)', font='Century', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.25)
plt.axvline(102, color='blue', linestyle=':', label='Max Range for 0.5 deg elevation angle and 1.5 km Clouds')
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
# Set the font name for axis tick labels to be Comic Sans
for tick in ax.get_xticklabels():
    tick.set_fontname("Century")
for tick in ax.get_yticklabels():
    tick.set_fontname("Century")
plt.legend(loc = 1, prop={'family': 'Century', 'size': 8})
plt.grid(True, alpha=0.25)

# Turn off top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.patch.set_alpha(0.95)

# Optionally turn off bottom and left spines
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.show()