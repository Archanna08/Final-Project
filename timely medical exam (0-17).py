
#Did not receive timely medical exam

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Denominator','Number_with_outcome')
for i in range(2081,2101):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
    
years = data.iloc[2081:2101,6]
outcome= data.iloc[2081:2101,9]
denominator= data.iloc[2081:2101,7]
percentage= outcome/denominator

#Plotting
plt.title("Percentage of medical exams done on ages 0-17 each year")
plt.plot(years,percentage,'o', linestyle='-')
