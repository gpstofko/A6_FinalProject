import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("antelope_data.csv")
x_1 = data["Annual Precipitation"]
x_2 = data["Winter Severity"]
x_3 = data["Adult Population"]
y = data["Fawn"]

fig, graph = plt.subplots(3)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Annual Precipitation")
graph[0].set_ylabel("Malaria")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Winter Severity")
graph[1].set_ylabel("Malaria")

graph[2].scatter(x_3, y)
graph[2].set_xlabel("Adult Population")
graph[2].set_ylabel("Malaria")

print("Correlation between Urban Population % and Malaria:",round(x_1.corr(y),2))
print("Correlation between Rural Population % and Malaria:",round(x_2.corr(y),2))
print("Correlation between % Access to basic sanitation serviced and Malaria:",round(x_3.corr(y),2))

plt.tight_layout()
plt.show()
