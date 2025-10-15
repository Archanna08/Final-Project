
#Did not receive timely medical exam

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Denominator','Number_with_outcome')
for i in range(2084,2102):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])
    
years = data.iloc[2081:2102,6] #Another way to filter the data (Used for line graph)
outcome= data.iloc[2081:2102,9]
denominator= data.iloc[2081:2102,7]
percentage= outcome/denominator

#Line Graph
plt.title("Percentage of medical exams not done on ages 0-17 each year")
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.plot(years,percentage,'o', linestyle='-')
plt.savefig("Timely_Exam_Line_Graph")

#Bar Graph
plt.title("Age group from 0 to 17 that did not Received Timely Medical exam ")
plt.xlabel('Year')
plt.ylabel('Number of outcomes')
for i in range(2084,2102):
    plt.bar(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], width=0.3, color='red')
<<<<<<< HEAD
<<<<<<< HEAD
    plt.grid(True)
     
#histogram
=======
=======
>>>>>>> 59c7ac49ade3f24c517eb7a7290497671889e5e3
plt.savefig("Timely_Exam_Bar_Graph")

#Description: 
#Both graphs tracks the number of children aged 0 to 17 years in the Child Welfare Department 
#who did not receive a timely medical exam between 1998 and 2023.
#Line graph shows results in percentage while the bar graph has exact numbers
#X-axis (Year): Spans from 1998 to 2023.
#Y-axis (Number of outcomes): Represents the number of children who did not receive a timely medical exam each year.
<<<<<<< HEAD
>>>>>>> 59c7ac49ade3f24c517eb7a7290497671889e5e3
=======
>>>>>>> 59c7ac49ade3f24c517eb7a7290497671889e5e3

