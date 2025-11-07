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

Used_Data= Raw_data[["Age_group", "Health_condition-Data_source", "Year", "Denominator", "Number_with_outcome", "Insurance", "Primary_Neighborhood"]]
Duplicates=pd.DataFrame.duplicated(Used_Data)
print(Duplicates.value_counts())
Used_Data=pd.DataFrame.drop_duplicates(Used_Data)

Used_Data=pd.DataFrame(Used_Data).dropna(subset=["Year"]) #dropna(subset) drops rows with null value in a certain column (subset)
null=pd.DataFrame.isnull(Used_Data[Used_Data["Year"]])
pd.Raw_dataFrame.sum(null)
#3. Univariate Non-Graphical EDA

#4. Univariate Graphical EDA

#5. Multivariate Non-Graphical EDA

#6. Multivariate Graphical EDA
#6.1 Statistical Relationships

#6.2 Categorical Raw_data

#6.3 Bivariate Distributions
