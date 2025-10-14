
#Did not receive timely medical exam

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Denominator','Number_with_outcome')
for i in range(2084,2102):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
    
years = data.iloc[2081:2102,6]
outcome= data.iloc[2081:2102,9]
denominator= data.iloc[2081:2102,7]
percentage= outcome/denominator

#Possible Plotting
plt.title("Percentage of medical exams done on ages 0-17 each year")
plt.plot(years,percentage,'o', linestyle='-')

plt.title("Age group from 0 to 17 that Received Timely Medical exam ")
plt.xlabel('Year')
plt.ylabel('Number of outcomes')
for i in range(2084,2102):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.3, color='red')


