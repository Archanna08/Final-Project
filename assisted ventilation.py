
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

#Pie Chart
plt.title("Percentage of assisted ventilation for babies (0-12 months)")
plt.pie(percentage,labels=years)
plt.savefig("Assisted_Ventilation_Pie_Chart")

#Bar Graph
plt.title("Assisted ventilation for babies(0-12 months)")
plt.xlabel('Year')
plt.ylabel('Number of outcomes')
for i in range(15, 25):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.3, color='green')
plt.savefig("Assisted_Ventilation_Bar_Graph")

#Description: 
#These figures show data from 2013 to 2022 presenting the number of newborns (0–12 months) 
#who required assisted ventilation immediately after birth.
#X values for bar graph and pie chart: Represents the years 2013 to 2022.
#Y-axis for bar graph: Number of newborns that needed assisted ventilation after birth

