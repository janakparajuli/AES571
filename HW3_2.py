import numpy as np
import matplotlib.pyplot as plt

# Define Radar Range Equation Parameters
MDS = -110   # dBm
C3 = 66.6    # dB, Radar Constant
L = -1       # dB, Radar Loss
r = np.linspace(1, 250, 250)  # Range from 1 to 250 km
# print(r)

# Calculate Mean Detectable Reflectivity (MDR)
MDR = C3 + MDS + 20 * np.log10(r) - L

# Plot MDR
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(r, MDR, color='red', linewidth=2)
ax.set_xlabel('Range (km)', font='Century Gothic', fontsize=12)
ax.set_ylabel('MDR (dBZ_e)', font='Century Gothic', fontsize=12)
ax.set_title('CHILL Radar: Minimum Detectable Reflectivity vs. Range (L = -1 dB)', font='Century Gothic', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axvline(172, color='blue', linestyle=':', label='Max Range for 1.5 km Clouds')
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
# Set the font name for axis tick labels to be Comic Sans
for tick in ax.get_xticklabels():
    tick.set_fontname("Century Gothic")
for tick in ax.get_yticklabels():
    tick.set_fontname("Century Gothic")
plt.legend(loc = 1, prop={'family': 'Century Gothic', 'size': 8})
plt.grid(True, alpha=0.25)


plt.show()