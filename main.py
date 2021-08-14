#importing pandas

import pandas as pd

#reading cdv file imported from kaggle (first comumn removed as not needed)
marketing_data = pd.read_csv("marketing_data.csv", index_col=0)
#subset of csv volumns printed below
print(marketing_data)



