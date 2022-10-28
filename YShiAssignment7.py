#import pandas and define function
import pandas as pd
def get_csv(web_link):
    data = pd.read_csv(web_link)
    return data

#read a web CSV and print the information
df = get_csv(r'https://data.cityofnewyork.us/resource/ymyu-3dbp.csv')
print(df.info())

#sum of tobacco cap data by regions
tobacco_cap_data = df.groupby("borough")[["tobacco_retail_dealer_cap_1"]].agg("sum")
print(tobacco_cap_data)

#import matplotlib and create bar plot
x = tobacco_cap_data.index
y = tobacco_cap_data["tobacco_retail_dealer_cap_1"]

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.barh(x,y,color = "maroon")
plt.title("Number of Tobacco Retail Dealer Cap by Region", fontsize=20, fontweight='bold')
plt.ylabel("Region", fontsize=15)
plt.xlabel("Number of Tobacco Retail Dealer Cap", fontsize=15)

