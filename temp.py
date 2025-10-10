# Final project
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

print(data["Number_with_outcome"])

plt.hist(data["Topic", "Number_with_outcome"].head(100))


# assisted ventilation
for i in range(17,27):
    print(data.iloc[i]['Age group'],data.iloc[i]['Year'], data.iloc[i]['Denominator'])