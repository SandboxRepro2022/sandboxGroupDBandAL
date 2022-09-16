import matplotlib.pyplot as plt
import pandas as pd

covidData = pd.read_csv('covid_agregated.txt')

plt.plot(covidData['V1'], covidData['V2'])
plt.show()