#Depression-Hopsital Admissions

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#Filtration
print('Age_group', 'Year','Insurance','Number_with_outcome')
for i in range(2986, 2998):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Insurance'],data.iloc[i]['Number_with_outcome'])

#Plotting
plt.figure(figsize=(9,5)) # size of the image
plt.suptitle('Insurance Type for Depression related hospital admission in children aged 0-18', fontweight='bold')
plt.subplots_adjust(hspace=0.3)
#2018    
plt.subplot(2, 2, 1) #number of row, # of columns, position
plt.pie([86, 101], labels=['Public', 'Private'], colors=['blue','purple'])
plt.title('2018')  

#2019
plt.subplot(2,2,2)
plt.pie([90,113], labels=['Public', 'Private'], colors=['blue','purple'] )
plt.title('2019')

#2020
plt.subplot(2,2,3)
plt.pie([92,98], labels=['Public', 'Private'], colors=['blue','purple'])
plt.title('2020')

#2021
plt.subplot(2,2,4)
plt.pie([92,102], labels=['Public', 'Private'], colors=['blue','purple'] )
plt.title('2020')

plt.savefig("Depression_Hospital_Admissions(0-18)_Pie_Subplots.png")
#Description: 
#This dataset presents the number of hospital admissions related to 
#depression among children and adolescents aged 0 to 18 years from 2018 to 2021, 
#classed according to the type of healthcare facility (Public, Private, and All).
#X-axis: Year (2018,2019,2020 and 2021)
#Y-axis: Number of hospital admissions
