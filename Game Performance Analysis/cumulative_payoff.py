import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
#data = data.loc[data['payoff'] <= 5]
gamelist = data.code.unique().tolist()
gamedict = {5901:'BBIN連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BBIN糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BBIN糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

try:
    gameid = int(input('請輸入你要求的遊戲:'))
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    requiredata = data[data.loc[:, "code"] == gameid]
    rawdata = requiredata.sort_values(by=['payoff']).dropna()
    #print(rawdata.tail(10))
    Total = rawdata['ct'].sum()
    Average = (rawdata['payoff'] * rawdata['ct']).sum() / Total
    print('Average={}'.format(Average))
    rawdata.loc[:, 'ctratio'] = rawdata.loc[:, 'ct'] / Total
    rawdata.loc[:, 'cumsum_ct'] = rawdata.loc[:, 'ctratio'].cumsum(axis= 0)
    Tail = rawdata[rawdata['cumsum_ct'] >=0.95]
    print(Tail.head(10))
    positions = np.array(rawdata[['payoff']]).flatten()
    frequencies = np.array(rawdata[['cumsum_ct']]).flatten()
    plt.scatter(positions, frequencies)
    plt.xlabel('payoff')
    plt.ylabel('count ratio')
    plt.title('Distribution of Payoffratio of {}'.format(gamedict[gameid]), fontproperties=font)
    plt.show()
except IndexError:
    print('請輸入正確的gaeeid')