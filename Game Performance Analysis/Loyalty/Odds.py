import pandas as pd
import numpy as np

df = pd.read_csv("bets_8690_11_06.csv")
data1 = df.drop("GameTypeId", axis =1)
data2 = data1.drop("RawDataType", axis =1)
data2.head()
data2['WagersTime'] = pd.to_datetime(data2['WagersTime'], format='%Y/%m/%d %H:%M')
data2['UpdatePayoffTime'] = pd.to_datetime(data2['UpdatePayoffTime'], format = '%Y/%m/%d %H:%M')
data3 = data2[data2['Commissionable'] != 0]
data = pd.pivot_table(data3, index = ['Commissionable', 'Payoff'])
print(data.head(30))