

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")


#filtration
print('Age_group', 'Period','Number_with_outcome') #titles
for i in range(2107,2133):
    print(data.iloc[i]['Age_group'],data.iloc[i]['Year'], data.iloc[i]['Period'],data.iloc[i]['Number_with_outcome'])

#Plotting
for i in range(2107,2133):
    plt.hist(data.iloc[2107:2133]['Number_with_outcome'], bins=6, color='skyblue', edgecolor='white')
    plt.title('Distribution of Number of teens(0-17) who received Individualized Program Education ')
    plt.ylabel('Number of years in each range')
    plt.xlabel('Number of teens who received Individualized Program Education')