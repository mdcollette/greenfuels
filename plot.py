## (C) Matthew Collette 2024
## See license file in repository for details

import pandas as pd
import matplotlib.pyplot as plt
ship_data = pd.read_csv('shipdata.csv', encoding='latin-1')

print(ship_data)
print (ship_data.dtypes)

ship_data['DWT'] = ship_data['DWT'].astype(float)
grouped_by_fuel = ship_data.groupby('Type of Fuel')

mfacecolor = ['green', 'purple', 'blue', 'none', 'black', 'red' ]

medgecolor = ['green', 'purple', 'blue', 'blue', 'black', 'red' ]

symbols = ['o', 'v', '*', '<', 'x', 's' ] # Change here to assign different symbols.

i = 0
plt.rcParams.update({'font.size': 24})
print(grouped_by_fuel)
fig, ax = plt.subplots(figsize=(12, 12))



for name, group in grouped_by_fuel:
    print(i)
    ax.plot(group['MJ Energy'], group['DWT'], label=name, markersize=15, markerfacecolor=mfacecolor[i], markeredgecolor=medgecolor[i], marker=symbols[i],  linestyle='')
    i = i + 1 

ax.tick_params(axis='both', which='major', length=15)
ax.tick_params(axis='both', which='minor', length=7)
plt.xlabel('Fuel Energy Stored Aboard, MJ')
plt.ylabel('Deadweight Capacity, MT')
plt.yscale('log')
plt.xscale('log')
plt.title('Are Batteries Going to Stunt Hydrogen?')
plt.legend()
plt.grid(True)
plt.savefig('current.png')