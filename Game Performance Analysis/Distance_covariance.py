import pandas as pd
import numpy as np


df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

for gameid in [5901, 5902, 5908, 21, 35]:
    rawdata = data[data.loc[:, "code"] == gameid].dropna().drop(columns=['code'])
    print(rawdata)