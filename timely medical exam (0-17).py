
#Did not receive timely medical exam

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Denominator','Number_with_outcome')
for i in range(2084,2101):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
    
    
#Plotting

plt.title("Age group from 0 to 17 that Received Timely Medical exam ")
plt.xlabel('Year')
plt.ylabel('Number of outcomes')
for i in range(2084,2101):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.3, color='blue')
   
