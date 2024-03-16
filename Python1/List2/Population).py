import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("CO2 emission.csv", sep=";")


countries = data.iloc[1:21,1].astype(str)
population = data.iloc[1:21, 4].str.replace(',', '').astype(float) 


plt.scatter(countries, population,color='skyblue')
plt.title("Country vs Population")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.xticks(rotation='vertical')
plt.tight_layout()

plt.savefig('country_vs_population.png')
plt.savefig('country_vs_population.jpeg')
plt.savefig('country_vs_population.svg')

plt.show()