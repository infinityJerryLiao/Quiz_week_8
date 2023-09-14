import matplotlib.pyplot as plt
import pandas as pd

climate_data = pd.read_csv('./climate.csv')

years = []
co2 = []
temp = []

for index, row in climate_data.iterrows():
    years.append(row["Year"])
    co2.append(row["CO2"])
    temp.append(row["Temperature"])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

