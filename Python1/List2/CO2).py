import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("CO2 emission.csv", sep=";")


countries = data.iloc[1:21,1].astype(str)
co2_emission = data.iloc[1:21, 2].str.replace(',', '').astype(float) 


plt.bar(countries, co2_emission, color='skyblue')
plt.title("CO2 Emissions by Country (2016)")
plt.xlabel("Countries")
plt.ylabel("CO2 Emissions (tons, 2016)")
plt.xticks(rotation='vertical')
plt.tight_layout()


plt.savefig('co2_emission_vs_countries.png')
plt.savefig('co2_emission_vs_countries.jpeg')
plt.savefig('co2_emission_vs_countries.svg')
plt.show()
