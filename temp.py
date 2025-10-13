# Final project
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")


#filtration
# assisted ventilation
print('Age_group', 'Year','Denominator','Number_with_outcome') #titles
for i in range(17,25):
    print(data.iloc[i]['Age_group'],data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
    
#iloc is used to choose the specific rows seeing on excel


#Plotting

plt.title("Assisted ventilation for babies(0-12 months)")
plt.xlabel('Year')
plt.ylabel('Number of outcomes')
for i in range(17, 25):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.3, color='green')
    plt.grid(True)

