import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
df = pd.read_csv("data_Odds.csv")
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['JoinTime'] = pd.to_datetime(df['JoinTime'], format = '%Y-%m-%d %H:%M:%S.%f')
df['mtt'] = pd.to_datetime(df['mtt'], format = '%Y-%m-%d')

rawdata1 = df[df['code'] == 5901].sort_values(by = ['memberid', 'date']).drop(columns=['mtt', 'JoinTime', 'code'])
aver1 = rawdata1['Odds'].sum() / rawdata1['Odds'].count()
print(rawdata1.head(100))
print(aver1)