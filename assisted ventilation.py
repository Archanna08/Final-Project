
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
percentage= outcome/denominator
#iloc is used to choose the specific rows seeing on excel

#Plotting
plt.pie(percentage,labels=years)
plt.title("Percentage of babies on assisted ventilation each year")



