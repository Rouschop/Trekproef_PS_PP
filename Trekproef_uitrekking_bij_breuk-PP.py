# Imports
import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt


#Parameters

breedte = 9.910  # mm
dikte = 4.04  # mm
oppervlakte = ((breedte/1000) * (dikte/1000))  # m^2
lengte = 80  # mm

# Create dataframe

headers = ['Time_[s]', 'Displacement_[mm]', 'Force_[kN]']
df = pd.read_csv('csv_files/tpe1_20211220_Trekproef_Jordy&Jordy_1_2_PP.csv',
                 names=headers,
                 sep=';',
                 skiprows=8,
                 dtype=float,
                 decimal=',')


# Prepare data

df['Force_[N]'] = df['Force_[kN]'].mul(1000)
df['Displacement_[m]'] = df['Displacement_[mm]'].div(1000)
df['Strain'] = df['Displacement_[mm]'].div(lengte)
df['Stress_[Pa]'] = df['Force_[N]'].div(oppervlakte)
df['Young_modulus_[Pa]'] = df['Stress_[Pa]'].div(df['Strain'])


# Define x & y data

x = df['Displacement_[mm]']
y = df['Force_[N]']

# Defining plot
plt.rcParams["figure.figsize"] = (15, 8)
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=5, color='b')

custom_font = 'Chandas'

ax.set_title('Uitrekking bij breuk PP', fontname=custom_font, size=24, weight="bold")
ax.set_xlabel('Verplaatsing [mm]', fontname=custom_font, size=22)
ax.set_ylabel('Kracht [N]', fontname=custom_font, size=22, fontweight="bold")
# plt.text(.0001, 3, 'Stress [Pa]', fontname=custom_font, size=20)

# Custom font x&y-ticks
for tick in ax.get_xticklabels():
    tick.set_fontname(custom_font)
    tick.set_size(12)

for tick in ax.get_yticklabels():
    tick.set_fontname(custom_font)
    tick.set_size(12)

# plt.show()
# Save fig
plt.savefig('Grafieken/uitrekking_bij_breuk_PP.jpg', dpi=300, pad_inches=1)
