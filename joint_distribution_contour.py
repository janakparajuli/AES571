# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Load data
# data = pd.read_csv('E:\\UAH_Classes\\Research\\Kansas\\PWS\\pws_in_complete.csv')
#
# # Convert temperature and dew point columns to numeric
# data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce')
# data['dewPoint'] = pd.to_numeric(data['dewpt'], errors='coerce')
#
# # Drop any rows where temperature or dew point data may be missing after conversion
# data.dropna(subset=['temperature', 'dewPoint'], inplace=True)
#
# # Plot joint distribution contour plot of temperature and dew point
# sns.kdeplot(data=data, x='temperature', y='dewPoint', cmap="Reds", fill=True, bw_adjust=.5)
# plt.title('Joint Distribution of Temperature and Dew Point')
# plt.xlabel('Temperature (°C)')
# plt.ylabel('Dew Point (°C)')
# plt.show()


import calplot
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('E:\\UAH_Classes\\Research\\Kansas\\PWS\\master_Kansas_pws_2024.csv')
data['obsTimeLocal'] = pd.to_datetime(data['obsTimeLocal'])
data.set_index('obsTimeLocal', inplace=True)

# Plot
calplot.calplot(data['temperature'], cmap='YlGnBu', suptitle='Daily Precipitation Rate')
plt.show()
