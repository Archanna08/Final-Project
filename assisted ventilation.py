
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")


#filtration
print('Age_group', 'Year','Denominator','Number_with_outcome') #titles
for i in range(15,25):
    print(data.iloc[i]['Age_group'],data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
years = data.iloc[15:25,6]
outcome= data.iloc[15:25,9]
denominator= data.iloc[15:25,7]
percentage= round(outcome/denominator*100, 2)
print(years, percentage, end=' ')
#iloc is used to choose the specific rows seeing on excel

# Possible Plotting
plt.title("Percentage of assisted ventilation for babies (0-12 months)")
plt.pie(percentage,labels=years)

plt.title("Assisted ventilation for babies(0-12 months)")
plt.xlabel('Year')
plt.ylabel('Number of outcomes')
for i in range(17, 25):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.3, color='green')
    plt.grid(True)

