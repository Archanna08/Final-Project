#Authorized psychotropic medications-child welfare

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Number_with_outcome')
for i in range(1914,1935):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])

#Scatter plotting
for i in range (1914,1935):
    plt.scatter(data.iloc[i]['Year'],data.iloc[i]['Number_with_outcome'], color='magenta')
    plt.xlabel('Year')
    plt.ylabel('Number of children ')
    plt.title('Authorized Psychotric medications from 2003-2013 for children(0-17)')
plt.grid(True)
plt.savefig("Authorized_Psychotic_Meds_Scatter_Graph")

#Description: 
#This scatter plots shows the trend in the number of children aged 0–17 under 
#Child Welfare who were authorized to receive psychotropic medications from 2003 to 2023.
#X-axis: Years from 2003-2023
#Y-axis: Number of children authorized for psychotropic medication
