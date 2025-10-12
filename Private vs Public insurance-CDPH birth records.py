#Private vs Public Insurance

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#Filtration
print("Year", "Total Births", "Public Insurance", "outcome")
for i in range(58510,58520):
    print(data.iloc[i]['Year'], data.iloc[i]["Denominator"], data.iloc[i]["Number_with_outcome"])

print("Year", "Total Births", "Private Insurance", "outcome")
for i in range(58292,58302):
    print(data.iloc[i]['Year'], data.iloc[i]["Denominator"], data.iloc[i]["Number_with_outcome"])  

#Plotting
plt.subplot(1,2,1)
plt.title("Private")
for i in range(58292, 58302):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.1, color='green')

plt.subplot(1,2,2)
plt.title("Public")
for i in range(58510,58520):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.1, color='red')

