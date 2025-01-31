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
plt.figure(figsize=(10, 6))
for band, lam in wavelengths.items():
    beamwidths = calculate_beamwidth(lam, D_values)
    plt.plot(D_values, beamwidths, label=f'{band} (λ={lam*100:.1f} cm)')

ax.set_title('Beamwidth vs. Reflector Diameter for Different Radar Bands')
plt.xlabel('Reflector Diameter (m)')
plt.ylabel('Beamwidth (degrees)')
plt.legend()
plt.grid(True)
plt.show()
