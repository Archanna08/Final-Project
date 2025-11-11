
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 20:43:04 2025

@author: Allison Leung, Archanna Nagesan
"""
import pandas as pd
import seaborn as sns

Raw_data=pd.read_csv("data.csv")

#2. Sorting, Filtering and Identifying Data
pd.DataFrame.info(Raw_data)
pd.DataFrame.describe(Raw_data)

Used_Data= Raw_data[["Age_group", "Health_condition-Data_source", "Sex", "Year", "Denominator", "Number_with_outcome", "Insurance", "Primary_Neighborhood", "Rate_SF_pop", "Race_ethnicity"]]
Duplicates=pd.DataFrame.duplicated(Used_Data)
print(Duplicates.value_counts())
Used_Data=pd.DataFrame.drop_duplicates(Used_Data)

Used_Data=pd.DataFrame(Used_Data).dropna(subset=["Year"]) #dropna(subset) drops rows with null value in a certain column (subset)
null=pd.DataFrame.isnull(Used_Data[Used_Data["Year"]])
pd.Raw_dataFrame.sum(null)
#3. Univariate Non-Graphical EDA
#numerical variable
num_variable= [ "Denominator", "Number_with_outcome", "Rate_SF_pop"]
num_summary = Used_Data.describe()
print(num_summary)
print(Used_Data[num_variable].skew())
print(Used_Data[num_variable].kurt())

#categorical variable
cat_variable= ["Age_group","Sex", "Health_condition-Data_source","Insurance", "Primary_Neighborhood", "Year", "Race_ethnicity"]
print(Used_Data[cat_variable].describe(include='object'))
#top=mode, freq count=count

#4. Univariate Graphical EDA
#Rate
sns.displot(data=Used_Data, x= 'Rate_SF_pop', multiple="stack", binrange= (0,200), hue="Race_ethnicity")
#Denominator
nia= Used_Data[(Used_Data["Sex"]!="ALL") & (Used_Data["Health_condition-Data_source"]=="ALL ER VISITS - ER VISITS")]
nia["percentage"]= nia["Number_with_outcome"]/nia["Denominator"]
sns.displot(data=nia, x= 'percentage', multiple="dodge", hue="Sex", binrange=(0,1.5))
for i in num_variable:
    sns.displot(data= Used_Data, x= i, hue= "Race_ethnicity", multiple= "stack")
#
#5. Multivariate Non-Graphical EDA

#6. Multivariate Graphical EDA
#6.1 Statistical Relationships

#6.2 Categorical Raw_data

#6.3 Bivariate Distributions