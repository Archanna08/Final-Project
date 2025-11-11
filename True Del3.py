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
Used_Data["Percentage"]=round(Used_Data["Number_with_outcome"]/Used_Data["Denominator"]*100, 2)
#Do this for every health condition we want
Assisted_Vent = Used_Data.iloc[15:25]
