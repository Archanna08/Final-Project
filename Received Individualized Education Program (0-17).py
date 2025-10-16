
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")


#filtration
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