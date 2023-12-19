import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("DatasetAfricaMalaria_2017.csv")
x = data[["Urban population (% of total population)","Rural population (% of total population)","People using at least basic sanitation services (% of population)"]].values
y = data["Incidence of malaria (per 1,000 population at risk)"].values
print(x)
print(y)

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)
#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y),2)
print(f"Model's Linear Equation: y={coef[0]}x1 + {coef[1]}x2 + {coef[2]}x3 + {intercept}") 
print("R Squared value:", r_squared)
#Loop through the data and print out the predicted prices and the 
#actual prices
predict = model.predict(xtest)
# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)
avg_percent_error=0.0
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    #x_coord = xtest[index] # gets the x value from the xtest dataset
    percent_error=abs((predicted_y-actual)/actual)*100
    avg_percent_error+=percent_error
    #print("x value:", float(x_coord), "Predicted y value:", predicted_y, "Actual y value:", actual)
avg_percent_error=avg_percent_error/(len(xtest))
print("average percent error:"+str(np.around(avg_percent_error,2))+"%")
print("***************")
print("Testing Results")
