import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("DatasetAfricaMalaria_2017.csv")
x_1 = data["People using at least basic sanitation services (% of population)"]
x_2 = data["Urban population (% of total population)"]
y = data["Incidence of malaria (per 1,000 population at risk)"]

fig, graph = plt.subplots(3)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("People using at least basic sanitation services (% of population)")
graph[0].set_ylabel("Malaria")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Urban population (% of total population)")
graph[1].set_ylabel("Malaria")


print("Correlation between People using at least basic sanitation services (% of population) and Malaria:",round(x_1.corr(y),2))
print("Correlation between Urban Population % and Malaria:",round(x_2.corr(y),2))


plt.tight_layout()
plt.show()
