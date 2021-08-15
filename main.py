#importing pandas

import pandas as pd

#reading cdv file imported from kaggle (first comumn removed as not needed)
df_marketing_data = pd.read_csv("marketing_data.csv", index_col=0)
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
print (df_marketing_data.mean())

print (cleaned_df_marketing_data.isna().sum())