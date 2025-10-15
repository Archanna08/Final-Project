

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")


#filtration
print('Age_group', 'Period','Number_with_outcome') #titles
for i in range(2107,2133):
    print(data.iloc[i]['Age_group'],data.iloc[i]['Year'], data.iloc[i]['Period'],data.iloc[i]['Number_with_outcome'])

#Plotting
for i in range(2107,2133):
    plt.hist(data.iloc[2107:2133]['Year'],data.iloc[2107:2133]['Number_with_outcome'], bins=10, color='skyblue', edgecolor='white')