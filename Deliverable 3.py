# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 20:43:04 2025

@author: Allison Leung ID: 2487300 sect.00003, Archanna Nagesan ID: 2482545 sect.00004 
Title: Health Outcomes of Mothers, Children, and Adolescents in San Francisco for a Decade (2013-2023) 
Programming in science – 420-SN1-RE  
Tiago Bortoletto Vaz  
Due Date: 16/11/2025  
"""
#This Python script performs data cleaning, filtering, and exploratory data analysis on San Francisco Health survey on mothers, children and youth.
#It also included both non-graphical summaries and graphical visualizations using Pandas and Seaborn.
import pandas as pd
import seaborn as sns

Raw_data=pd.read_csv("data.csv")

#2. Sorting, Filtering and Identifying Data
Used_Data= Raw_data[["Age_group", "Health_condition-Data_source", "Sex", "Year", "Denominator", "Number_with_outcome", "Insurance", "Primary_Neighborhood", "Rate_SF_pop", "Race_ethnicity"]]
pd.DataFrame.info(Used_Data)
pd.DataFrame.describe(Used_Data)
pd.DataFrame.nunique(Used_Data)
print(Used_Data["Year"].value_counts())

pd.DataFrame.duplicated(Used_Data).value_counts()
Used_Data=pd.DataFrame.drop_duplicates(Used_Data)

Used_Data=pd.DataFrame(Used_Data).dropna(subset=["Year"]) #dropna(subset) drops rows with null value in a certain column (subset)
print(pd.DataFrame.isnull(Used_Data["Year"]).sum()) #To check if the rows were dropped

    #The sub-datasets that are used for the graphs to answer specific questions
G_Screentime = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='3 OR MORE HOURS SCREENTIME - YRBS SURVEY') & (Used_Data['Age_group'] !='GRADE6to8')]
G_All_ER_visits = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='ALL ER VISITS - ER VISITS')]
G_Depression_admissions = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='DEPRESSION - HOSPITAL ADMISSIONS')]
G_Pub_Pri_Insurance = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='PUBLIC INSURANCE - CDPH BIRTH RECORDS') 
                                  | (Used_Data['Health_condition-Data_source']=='PRIVATE INSURANCE - CDPH BIRTH RECORDS')]
        # | is equivalent to or 
G_Alcohol = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='ALCOHOL - ER VISITS')]
G_Al_fil = G_Alcohol[G_Alcohol['Primary_Neighborhood'] != 'All'] #Just for 6.2 j)
G_Timely_med_exam = Used_Data.loc[Used_Data['Health_condition-Data_source']=='DID NOT RECEIVE TIMELY MEDICAL EXAM - CHILD WELFARE']
G_HIV_tests = Used_Data.loc[(Used_Data['Health_condition-Data_source']=='NEVER TESTED FOR HIV - YRBS SURVEY') & (Used_Data['Age_group'] != 'GRADE9to12')]

    #Sub-datasets for Multiv. non-graph EDA (Gets rid of 'All' as a varible in specified column)
Data_sex = Used_Data.loc[Used_Data['Sex'] != 'ALL']
Data_Neighborhood = Used_Data.loc[(Used_Data['Primary_Neighborhood'] != 'All') & (Used_Data['Primary_Neighborhood'] != 'ALL')]
Data_Insurance = Used_Data.loc[Used_Data['Insurance'] != 'ALL']

#3. Univariate Non-Graphical EDA
    #numerical variable
variable_num= [ "Denominator", "Number_with_outcome", "Rate_SF_pop"]
var_num_summary = Used_Data[variable_num].describe()
print(var_num_summary)
print(Used_Data[variable_num].skew(), Used_Data[variable_num].kurt(), Used_Data[variable_num].mode(),Used_Data[variable_num].var())

    #categorical variable
variable_cat= ["Age_group","Sex", "Health_condition-Data_source","Insurance", "Primary_Neighborhood", "Year", "Race_ethnicity"]
pd.set_option('display.max_columns', None) #function to display all columns
print(Used_Data[variable_cat].astype(str).describe()) #converting year as strings
       #top=mode, freq count=count
       
#4. Univariate Graphical EDA
for i in variable_num: #Not all the graphs generated here are used
    sns.displot(data=G_HIV_tests, x=i, multiple="dodge", hue="Sex", bins=35)
    sns.displot(data=G_HIV_tests, x=i, multiple="stack", hue="Age_group")
    sns.displot(data=G_HIV_tests, x=i, kind="kde", hue="Year", bw_adjust=.5)
    sns.displot(data=G_HIV_tests, x=i, hue="Year", element="step", stat='density')
    sns.displot(data=G_HIV_tests, x=i, hue="Sex", kind="ecdf")

#5. Multivariate Non-Graphical EDA
#a
pd.crosstab(Data_Neighborhood["Primary_Neighborhood"], Data_Neighborhood["Sex"])
pd.crosstab(Data_Neighborhood["Primary_Neighborhood"], Data_Neighborhood["Year"])
NG_Race_Insur = pd.crosstab(Data_Insurance["Race_ethnicity"], Data_Insurance["Insurance"])
print(NG_Race_Insur)
#b
pd.crosstab(Data_Insurance["Age_group"],Data_Insurance["Insurance"], normalize='index' )*100 #percentage
#c
NG_Sex_Age_Insur = pd.crosstab([Data_sex["Age_group"], Data_sex["Sex"]], columns= Data_sex["Insurance"])
print(NG_Sex_Age_Insur)

print(pd.DataFrame.nunique(Data_sex)) #DELETE AFTER, JUST USED FOR CHECKING
#6. Multivariate Graphical EDA
    #6.1 Statistical Relationships
#a
g= sns.relplot( data=G_All_ER_visits , x='Denominator', y='Number_with_outcome', col='Sex')
g.fig.suptitle('Number of People who Visited the ER', y=1.1)
#b
g=sns.relplot(data= G_Depression_admissions, x= 'Number_with_outcome', y='Denominator', hue='Sex', col='Year', size='Age_group', col_wrap=3)
g.fig.suptitle('Number of People that got Admitted for Depressions in the Survey', y=1.05)
#c
sns.relplot(data=G_Timely_med_exam, x='Year',y='Rate_SF_pop', kind='line').set(title='Percentage of Children getting Timely Medical Exams from 1998-2023')
#d 
sns.relplot(data= G_Alcohol, x='Year', y='Number_with_outcome', kind='line',errorbar='sd', height=4,aspect=2).set(title='Number of People using Alcohol among People who took the Survey')
#e
sns.lmplot(data = G_Pub_Pri_Insurance , x= 'Denominator', y='Number_with_outcome', hue='Health_condition-Data_source').set(title='Number of Pregnant Women with Different Insurances from CDPH Birth Records')

    #6.2 Categorical data
#a 
sns.catplot(data=G_Timely_med_exam , x= 'Year', y='Rate_SF_pop', jitter= False,  height=4,aspect=4 ).set(title='Percentage of Timely Medical Exam from 1998-2023')

#b
sns.catplot(data= G_Depression_admissions, x='Year', y='Number_with_outcome', jitter=True).set(title='Number of Depression Admissions from 2017-2021')
#c
sns.catplot(data= G_HIV_tests, x='Year', y='Number_with_outcome', hue='Sex').set(title='Number of Students that havent taken the HIV test')
#d
sns.catplot(data= G_HIV_tests , x= 'Sex', y= 'Number_with_outcome', hue='Age_group', kind='box').set(title='Percentage of Age group that never took the HIV test')
#e
sns.catplot(data= G_Depression_admissions, x='Year', y='Number_with_outcome', kind='boxen').set(title='Number of People that got Admitted for Depressions from 2017-2021')
#f
sns.catplot( data=G_All_ER_visits, x='Year', y='Rate_SF_pop',  hue='Sex', kind='violin', split = True ).set(title='Percentage of People that went to the ER from 2017-2021')
#g
g=sns.catplot( data= G_Screentime, x='Age_group', y='Number_with_outcome', kind='violin', inner=None)
sns.swarmplot( data= G_Screentime, x='Age_group', y='Number_with_outcome', color='k', ax=g.ax).set(title='Percentage of Middle schoolers Screentime')
#h 
sns.catplot(data= G_Depression_admissions, x='Year', y='Number_with_outcome',hue='Insurance', kind='bar', errorbar=('pi',97)).set(title='Number of People Admitted for Depression and their Insurance')  
#i 
sns.catplot(data= G_Pub_Pri_Insurance, x='Health_condition-Data_source',y='Rate_SF_pop', hue='Sex', errorbar=('pi', 90), kind='point', height=4,aspect=2 ).set(title='Percentage of People with Public Insurance vs Private')
#j
j= sns.catplot(data= G_Al_fil, x="Primary_Neighborhood",hue= 'Primary_Neighborhood', kind='count',height=10, aspect=5.5)
j.fig.suptitle('The number of neighborhoods surveyed for alcohol use', fontsize=24)


    #6.3 Bivariate Distributions
#a
sns.displot(data= G_Screentime, x='Denominator', y='Number_with_outcome', binwidth=(60,50), cbar=True).set(title='Middle Schoolers Screentime')
#b
sns.displot(data= G_Pub_Pri_Insurance, x='Year', y='Rate_SF_pop',kind='kde').set(title='Percentage of People with Public vs Private Insurance')
#c 
sns.displot(data= G_Alcohol, x='Year', y='Rate_SF_pop',hue='Sex',kind='kde').set(title='Percentage of people who used alcohol from 2016-2022')
