#Authorized psychotropic medications-child welfare

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Number_with_outcome')
for i in range(1914,1935):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])

#Scatter plotting
for i in range (1914,1935):
    plt.scatter(data.iloc[i]['Year'],data.iloc[i]['Number_with_outcome'], color='magenta')
    plt.xlabel('Year')
    plt.ylabel('Number with condition')
    plt.title('Number of Authorized Psychotric medications from 2003-2013 for children(0-17)')
    

    