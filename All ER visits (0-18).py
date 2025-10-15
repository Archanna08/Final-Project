#All ER visits (0-18)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

data = pd.read_csv("data.csv")

#Filtration

print('Age_group', 'Year','Number_with_outcome')
for i in range(2293,2305):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Insurance'],data.iloc[i]['Number_with_outcome'])

#Plotting- Scatter
for i in range (2293,2305):
    plt.plot(data.iloc[i]['Year'],data.iloc[i]['Number_with_outcome'],linestyle='-')
    if data.iloc[i]['Insurance']== 'ALL':
        plt.scatter(data.iloc[i]['Year'],data.iloc[i]['Number_with_outcome'], color='orange')
        plt.plot(data.iloc[2293:2304]['Year'], data.iloc[2293:2304]['Number_with_outcome'], linestyle='-', color='black')
plt.xlabel('Year')
plt.ylabel('Number of ER visits')
plt.title('Number of ER visits for safety purposes from 2003-2013 for children(0-18)')

#IM TIRED OF THIS PLZ WORK