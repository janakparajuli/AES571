import numpy as np
import matplotlib.pyplot as plt

# Wavelengths in meters
wavelengths = {'Ka-band': 1.0e-2, 'Ku-band': 1.8e-2, 'X-band': 3.0e-2, 'C-band': 5.5e-2}
D_values = np.linspace(0.3, 9, 300)  # Diameter from 0.3 m to 9 m
beamwidth_constant = np.sqrt(1.6)

# Function to calculate beamwidth
def calculate_beamwidth(lam, D):
    return beamwidth_constant * (lam / D) * (180 / np.pi)  # Convert to degrees

# Plotting
fig,ax = plt.subplots(figsize=(10, 6))
for band, lam in wavelengths.items():
    beamwidths = calculate_beamwidth(lam, D_values)
    plt.plot(D_values, beamwidths, label=f'{band} (λ={lam*100:.1f} cm)')

ax.set_title('Beamwidth as a function of Reflector Diameter for Different Radar Bands', font='Century Gothic', fontsize=14)
ax.set_xlabel('Reflector Diameter (m)', font='Century Gothic', fontsize=12)
ax.set_ylabel('Beamwidth (degrees)', font='Century Gothic', fontsize=12)
ax.axhline(y=1, linestyle = '--', alpha=0.25)
ax.text(-0.33, 1, '1', va='center', ha='center', font='Century Gothic', fontsize=12)
ax.axhline(y=2, linestyle = '--', alpha=0.25)

ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
# Set the font name for axis tick labels to be Comic Sans
for tick in ax.get_xticklabels():
    tick.set_fontname("Century Gothic")
for tick in ax.get_yticklabels():
    tick.set_fontname("Century Gothic")
plt.legend(title='Wavelengths', loc = 1, prop={'family': 'Century Gothic', 'size': 8})
plt.grid(True, alpha=0.25)
plt.show()
