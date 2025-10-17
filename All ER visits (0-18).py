#All ER visits (0-18)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#Filtration

print('Age_group', 'Year','Number_with_outcome') #The for loop is used to check the data we want to extract.
for i in range(2251,2266):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Insurance'],data.iloc[i]['Number_with_outcome'])

years = data.iloc[[2251, 2254, 2257, 2260, 2263],6] #Another way to filter the data for graph
outcome= data.iloc[[2251, 2254, 2257, 2260, 2263],9] #Uses iloc to select certain rows (in smaller []) and column (after ,)

#Line Graph
plt.plot(years, outcome, color='orange', linestyle='-', marker='o')
plt.xlabel('Year')
plt.ylabel('Number of ER visits')
plt.title('ER visits for safety purposes from 2017-2021 for ages(0-18)')
plt.grid(True)
plt.savefig("All_ER_Visits(0-18)_Line_Graph")

#Description: 
#This scatter plot shows data from 2017 to 2021 presenting the number of ER visits
#done by children (0-18) for safety purposes without considering the type of insurance. 
#X-axis: Years from 2017-2021
#Y-axis: Number of ER visits
