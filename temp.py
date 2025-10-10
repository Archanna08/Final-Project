# Final project
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

print(data["Number_with_outcome"])

plt.hist(data["Topic", "Number_with_outcome"].head(100))

#filtration
# assisted ventilation
print('Age_group', 'Year','Denominator','Number_with_outcome') #titles
for i in range(17,25):
    print(data.iloc[i]['Age_group'],data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
    
#iloc is used to choose the specific rows seeing on excel


#Plotting