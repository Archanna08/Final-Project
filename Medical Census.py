# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 21:57:29 2025

@author: Allison Leung, Archanna Nagesan

This script includes all the graphs for the dataset that includes San Francesco censuses over multiple years 
about different medical conditions
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#1. Assisted ventilation
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
#These figures show data from 2013 to 2022 presenting the number of newborns (0–12 months) who required assisted ventilation immediately after birth.
#X values for bar graph and pie chart: Represents the years 2013 to 2022.
#Y-axis for bar graph: Number of newborns that needed assisted ventilation after birth


#2. All ER visits (0-18)
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
#This scatter plot shows data from 2017 to 2021 presenting the number of ER visits done by children (0-18) for safety purposes without considering the type of insurance. 
#X-axis: Years from 2017-2021
#Y-axis: Number of ER visits


#3. Authorized psychotropic medications-child welfare (0-17)
print('Age_group', 'Year','Number_with_outcome')
for i in range(1914,1935):
    print(data.iloc[i]['Age_group'], data.iloc[i]['Year'], data.iloc[i]['Denominator'],data.iloc[i]['Number_with_outcome'])

#Scatter plotting
for i in range (1914,1935):
    plt.scatter(data.iloc[i]['Year'],data.iloc[i]['Number_with_outcome'], color='magenta')
    plt.xlabel('Year')
    plt.ylabel('Number of children ')
    plt.title('Authorized Psychotric medications from 2003-2013 for children(0-17)')
plt.grid(True)
plt.savefig("Authorized_Psychotic_Meds_Scatter_Graph")

#Description: 
#This scatter plots shows the trend in the number of children aged 0–17 under Child Welfare who were authorized to receive psychotropic medications from 2003 to 2023.
#X-axis: Years from 2003-2023
#Y-axis: Number of children authorized for psychotropic medication


#Depression-Hopsital Admissions (0-18)
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
plt.pie([92,102],labels=['Public', 'Private'], colors=['blue','purple'] )
plt.title('2021')

plt.savefig("Depression_Hospital_Admissions(0-18)_Pie_Subplots.png")
#Description: 
#This dataset presents the number of hospital admissions related to depression among children and adolescents aged 0 to 18 years from 2018 to 2021, 
#classed according to the type of healthcare facility (Public, Private, and All).
#X-axis: Year (2018,2019,2020 and 2021)
#Y-axis: Number of hospital admissions


#Private vs Public Insurance
print("Year", "Total Births", "Public Insurance", "outcome")
for i in range(58510,58520):
    print(data.iloc[i]['Year'], data.iloc[i]["Denominator"], data.iloc[i]["Number_with_outcome"])

print("Year", "Total Births", "Private Insurance", "outcome")
for i in range(58292,58302):
    print(data.iloc[i]['Year'], data.iloc[i]["Denominator"], data.iloc[i]["Number_with_outcome"])  

#Plotting of Private Insurance
plt.subplot(2,1,1)
plt.title("Private insurance")
for i in range(58292, 58302):
    plt.barh(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], height=0.3, color='green')
plt.xlabel("Number of Births")
plt.ylabel("Year")

#Plotting of Public Insurance
plt.subplot(2,1,2)
plt.title("Public insurance")
for i in range(58510,58520):
    plt.barh(data.iloc[i]['Year'], data.iloc[i]['Number_with_outcome'], height=0.3, color='red')
plt.xlabel("Number of Births")
plt.ylabel("Year")

plt.subplots_adjust(hspace=0.7)
plt.suptitle("Pregnant women who have private vs public insurance", fontweight='bold')
plt.savefig("Public_vs_Private_Insurance_Bar_Sub-plots")

#Description: 
#This figure contains two bar charts (subplots) comparing the number of births covered by private and public insurance from 2013 to 2022.
#X-axis (Year): Range of years from 2013 to 2022.
#Y-axis (Number of births with outcome): Represents the number of recorded birth outcomes each year.


#Received Individualized Education Program (0-17)
print('Age_group', 'Period','Number_with_outcome') 
for i in range(2107,2133):
    print(data.iloc[i]['Age_group'],data.iloc[i]['Year'], data.iloc[i]['Period'],data.iloc[i]['Number_with_outcome'])

#Plotting
plt.figure(figsize=(9,5))
for i in range(2107,2133):
    plt.hist(data.iloc[2107:2133]['Number_with_outcome'], bins=6, color='skyblue', edgecolor='white')
    plt.title('Distribution of Number of teens(0-17) who received Individualized Program Education', size=12, fontweight='bold', )
    plt.ylabel('Number of years that fall in each range')
    plt.xlabel('Range of Number of teens who received Individualized Program Education')
plt.savefig("Recieived_Individual_Education_Histogram")
#Description: This histogram shows the distribution of the number of teens (ages 0–17) who received Individualized Program Education over the years 1998–2023.
#In short, it summarizes how frequently the yearly counts fell into different ranges, highlighting periods with higher or lower numbers of teens receiving Individualized Program Education.
#X-axis: Ranges of the number of teens who received Individualized Program Education (e.g., 50–100, 100–150, …).
#Y-axis: Number of years in which the number of teens fell into each range.


#Did not receive timely medical exam (0-17)
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
    plt.grid(True)     
plt.savefig("Timely_Exam_Bar_Graph")

#Description: 
#Both graphs tracks the number of children aged 0 to 17 years in the Child Welfare Department who did not receive a timely medical exam between 1998 and 2023.
#Line graph shows results in percentage while the bar graph has exact numbers
#X-axis (Year): Spans from 1998 to 2023.
#Y-axis (Number of outcomes): Represents the number of children who did not receive a timely medical exam each year.

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