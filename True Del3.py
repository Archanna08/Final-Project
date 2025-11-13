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
    #Overall filtered dataset that we're gonna use
Used_Data=pd.DataFrame(Used_Data).dropna(subset=["Year"]) #dropna(subset) drops rows with null value in a certain column (subset)
print(pd.DataFrame.isnull(Used_Data["Year"]).sum()) #To check if the rows were dropped
Used_Data["Percentage"]=round(Used_Data["Number_with_outcome"]/Used_Data["Denominator"]*100, 2)

    #The sub-datasets that are used for the graphs to answer specific questions
Assisted_Vent = Used_Data.iloc[4:14]
All_ER_visits = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='ALL ER VISITS - ER VISITS')]
Authorized_meds = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='AUTHORIZED FOR PSYCHOTROPIC MEDICATIONS - CHILD WELFARE') & (Used_Data['Age_group']=='0to17')]
Depression_admissions = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='DEPRESSION - HOSPITAL ADMISSIONS')]
Pub_Pri_Insurance = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='PUBLIC INSURANCE - CDPH BIRTH RECORDS') 
                                  | (Used_Data['Health_condition-Data_source']=='PRIVATE INSURANCE - CDPH BIRTH RECORDS')]
        # | is equivalent to or 
Ind_Edu = Used_Data.loc[Used_Data['Health_condition-Data_source']=='RECEIVED INDIVIDUALIZED EDUCATION PROGRAM - CHILD WELFARE']
Timely_med_exam = Used_Data.loc[Used_Data['Health_condition-Data_source']=='DID NOT RECEIVE TIMELY MEDICAL EXAM - CHILD WELFARE']

#Note to archanna: maybe??? if we need; compare different grades
HIV_tests = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='NEVER TESTED FOR HIV - YRBS SURVEY') & (Used_Data['Age_group'] != 'GRADE9to12')]

#3. Univariate Non-Graphical EDA
    #numerical variable
num_variable= [ "Denominator", "Number_with_outcome", "Rate_SF_pop", "Percentage"]
num_summary = Used_Data.describe()
print(num_summary)
print(Used_Data[num_variable].skew(), Used_Data[num_variable].kurt())

    #categorical variable
cat_variable= ["Age_group","Sex", "Health_condition-Data_source","Insurance", "Primary_Neighborhood", "Year", "Race_ethnicity"]
print(Used_Data[cat_variable].describe(include='object'))
       #top=mode, freq count=count

#4. Univariate Graphical EDA
for i in num_variable:
    sns.displot(data=Pub_Pri_Insurance, x=i, multiple="dodge", hue="Health_condition-Data_source", bins=35)
    sns.displot(data=HIV_tests, x=i, multiple="stack", hue="Age_group")
    sns.displot(data=Depression_admissions, x=i, kind="kde", hue="Year", bw_adjust=.5)
    sns.displot(data=All_ER_visits, x=i, hue="Year", element="step", stat='density')
    sns.displot(data=Authorized_meds, x=i, kind="ecdf")

#5. Multivariate Non-Graphical EDA

#6. Multivariate Graphical EDA
    #6.1 Statistical Relationships

    #6.2 Categorical Raw_data

    #6.3 Bivariate Distributions
