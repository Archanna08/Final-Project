import seaborn as sns

sns.set_theme()
tips= sns.load_dataset('tips') 

sns.relplot(data= tips, x='total_bill', y= 'tip')

fmri=sns.load_dataset('fmri')
sns.relplot( data=fmri, kind= 'line',x='timepoint',y='signal', col='region',hue='event', style='event')

#3 a)

life_expectancy= sns.load_dataset('healthexp')
sns.relplot(data=life_expectancy, x='Spending_USD', y='Life_Expectancy')

#3 b)

#filtration
life_expectancy_can = life_expectancy[life_expectancy['Country'] == 'Canada']
sns.lmplot(data= life_expectancy_can, x='Spending_USD', y='Life_Expectancy')

#3 c)

sns.relplot(data=life_expectancy , x= 'Spending_USD', y= 'Year')

#3 d)
sns.relplot(data=life_expectancy , x= 'Spending_USD', y= 'Year', hue= 'Country')

#3 e)
sns.relplot(data=life_expectancy , x= 'Spending_USD', y= 'Life_Expectancy', hue= 'Year', col='Country')