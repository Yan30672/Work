import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from pylab import *

zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\kaiu.ttf')
pd.set_option('display.max_columns', None)
df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
data.loc[:, 'payoff'] = round(data.loc[:, 'payoff'], 1)
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


rawdata1 = data[data.loc[:, "code"] == 5901].dropna().groupby('payoff')['ct'].sum().reset_index(name='Count')
total1 = rawdata1['Count'].sum()