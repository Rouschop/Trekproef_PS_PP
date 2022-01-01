# Imports
import pandas as pd
import matplotlib.pyplot as plt


#Parameters

breedte = 9.910/1000  # m
dikte = 4.04/1000  # m
oppervlakte = breedte * dikte  # m^2
lengte = 0.08  # m

# Create dataframe

headers = ['Time_[s]', 'Displacement_[mm]', 'Force_[kN]']
df = pd.read_csv('csv_files/tpe1_20211220_Trekproef_Jordy&Jordy_2_2_PS.csv',
                 names=headers,
                 sep=';',
                 skiprows=8,
                 dtype=float,
                 decimal=',')


# Prepare data

df['Force_[N]'] = df['Force_[kN]'].mul(1000)
df['Displacement_[m]'] = df['Displacement_[mm]'].div(1000)
df['Strain'] = df['Displacement_[m]'].div(lengte)
df['Stress_[Pa]'] = df['Force_[N]'].div(oppervlakte)
df['Young_modulus_[Pa]'] = df['Stress_[Pa]'].div(df['Strain'])
df['%_Strain'] = df['Displacement_[m]'].div(lengte) * 100

# Define data

x = df['Strain']
y = df['Stress_[Pa]']

# Defining plot
plt.rcParams["figure.figsize"] = (15, 8)
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=5, color='b')

custom_font = 'Chandas'

ax.set_title('Young modulus PS', fontname=custom_font, size=24, weight="bold")
ax.set_xlabel('Strain [-]', fontname=custom_font, size=22)
ax.set_ylabel('Stress [Pa]', fontname=custom_font, size=22, fontweight="bold")
# plt.text(.0001, 3, 'Stress [Pa]', fontname=custom_font, size=20)

# Custom font x&y-ticks
for tick in ax.get_xticklabels():
    tick.set_fontname(custom_font)
    tick.set_size(12)

for tick in ax.get_yticklabels():
    tick.set_fontname(custom_font)
    tick.set_size(12)

# plt.show()
plt.savefig('Grafieken/Young_modulus_PS.jpg', dpi=300, pad_inches=1)
# print(df['Displacement_[mm]'])

# df.to_csv('trekproef_PS.csv')
