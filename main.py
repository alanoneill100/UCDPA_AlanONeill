#importing pandas

import pandas as pd

#reading csv file imported from kaggle (first comumn removed as not needed)
df_marketing_data = pd.read_csv("marketing_data.csv")
#subset of csv volumns printed below
print(df_marketing_data)

#showing type below (dataframe)
print(type(df_marketing_data))

#Analysing dataframe
print(df_marketing_data.head())   #prints first 5 columns
print(df_marketing_data.shape)
#2,240 rows and 27 columns

#Missing values
print(df_marketing_data.info())
print (df_marketing_data.isna().sum())

#Option 1 - Drop missing values
#cleaned_df_marketing_data = df_marketing_data.dropna()
#cleaned_df_marketing_data = df_marketing_data.dropna(axis=1)
#print(df_marketing_data.shape, cleaned_df_marketing_data.shape)

#Option 2 - Replace missing values
cleaned_df_marketing_data = df_marketing_data.fillna(0)
#print(df_marketing_data.shape, cleaned_df_marketing_data.shape)
print (cleaned_df_marketing_data.isna().sum())
#print (df_marketing_data.mean())

print (cleaned_df_marketing_data.isna().sum())

#Dropping Duplicates
print(cleaned_df_marketing_data.shape)
cleaned_df2_marketing_data= df_marketing_data.drop_duplicates(subset=[" Income "])
print(cleaned_df2_marketing_data.shape)
print(df_marketing_data['ID'])


#For Loops, iterrows
for lab, row in df_marketing_data.iterrows():
     print(str(lab) + ":" + row["Education"])

#Merging Dataframes
df_water = pd.read_csv("water_potability.csv")

#result = pd.merge (df_marketing_data, df_water [ ["Year_Birth", 'ph', 'Sulfate']],
                   #on="Year_Birth")
#result.head(5)

frames = [df_water, df_marketing_data]
result = pd.concat(frames)
print(result)
print(result.info())

#Writing a custom function
def my_ucd_function():
     print("This is a custom function")

print(my_ucd_function())

def max(x,y):
     if x + y == 3:
          return x
     else:
          return y

print( max(1,2))

#custom function related to project dataset
def ID_Column_Subset():
     print(df_marketing_data['ID'].head(4))

print(ID_Column_Subset())


#Numpy
import numpy as np
list_1 = df_water["Organic_carbon"].head(6)
print(list_1)
list_1a = list_1.values.tolist()
print(list_1a)
print(list_1)

list_2 = df_marketing_data["ID"].head(6)
print(list_2)
list_2a = list_2.values.tolist()
print(list_2a)

#converting lists to mupy arrays
np_list_1a = np.array(list_1a)
print(np_list_1a)
print(type(np_list_1a))

np_list_2a = np.array(list_2a)
print(np_list_2a)
print(np_list_1a + np_list_2a)

#Visualising Data - Matplotlib
import matplotlib.pyplot as plt
fig,ax = plt.subplots()

x = cleaned_df_marketing_data["Year_Birth"].head(10)
y1 = cleaned_df_marketing_data["MntWines"].head(10)
y2 = cleaned_df_marketing_data ["MntMeatProducts"].head(10)
ax.plot (x,y1, marker = "o",linestyle="--", color="b", linewidth = 4.0)
ax.plot (x, y2, marker = "v", linestyle="--", color="g")
plt.title ('Analysis of Grocery Consumption')
ax.set(xlabel = "Year of Birth", ylabel = "Consumption of Wine and Meat Products")
plt.show()


