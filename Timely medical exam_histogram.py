

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")

#filtration
print('Age_group', 'Year','Denominator','Number_with_outcome')
for i in range(2084,2102):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])

#histogram
for i in range(2084,2102):
    plt.hist(data.iloc[2084:2102]['Number_with_outcome'], bins=9, color='teal')
    plt.title('Distribution of number of assisted timely medical exam from 2001 to 2018')
    plt.xlabel('Number of assisted timely medical exam')
    plt.ylabel('Number of years')
plt.savefig("Timely_Exam_Histogram.png")

#Description: 
#This histogram illustrates the distribution of the number of children aged 0–17 
#who did not receive a timely medical exam while under the care of 
#the Child Welfare Department or Probation-supervised care between 1998 and 2023.
#x-axis: Number of children without a timely medical exam
#y-axis: the frequency of years in which those values occurred.