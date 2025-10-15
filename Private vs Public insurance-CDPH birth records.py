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

#Plotting of Private Insurance
plt.subplot(2,1,1)
plt.title("Private insurance")
for i in range(58292, 58302):
    plt.barh(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], height=0.3, color='green')
plt.xlabel("Number of Births")
plt.ylabel("Year")

#Plotting of Public Insurance
plt.subplot(2,1,2)
plt.title("Public insurance")
for i in range(58510,58520):
    plt.barh(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], height=0.3, color='red')
plt.xlabel("Number of Births")
plt.ylabel("Year")

plt.subplots_adjust(hspace=0.7)
plt.suptitle("Pregnant women who have private vs public insurance", fontweight='bold')
plt.savefig("Public_vs_Private_Insurance_Bar_Sub-plots")

#Description: 
#This figure contains two bar charts (subplots) comparing 
#the number of births covered by private and public insurance from 2013 to 2022.
#X-axis (Year): Range of years from 2013 to 2022.
#Y-axis (Number of births with outcome): Represents the number of recorded birth outcomes each year.

