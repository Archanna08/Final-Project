#Depression-Hopsital Admissions

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#Filtration
print('Age_group', 'Year','Insurance','Number_with_outcome')
for i in range(2986, 2998):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Insurance'],data.iloc[i]['Number_with_outcome'])

#Plotting