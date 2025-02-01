import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('E:\\UAH_Classes\\Research\\Kansas\\PWS\\master_Kansas_pws_2024.csv')

# Plot
sns.kdeplot(data['temperature'], data['dewpt'], cmap="Reds", shade=True, bw_adjust=.5)
plt.title('Joint Distribution of Temperature and Dew Point')
plt.xlabel('Temperature (°C)')
plt.ylabel('Dew Point (°C)')
plt.show()
