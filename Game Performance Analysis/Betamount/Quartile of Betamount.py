import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math

pd.set_option('display.max_columns', None)
df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


for gameid in [5901, 5902, 5908, 21, 35]:
    rawdata = data[data['code'] == gameid].dropna().groupby('betamount')['ct'].sum().reset_index(name='count')
    total = rawdata['count'].sum()
    mean = (rawdata['betamount'] * rawdata['count']).sum() / total
    rawdata.loc[:, 'ratio'] = rawdata.loc[:, 'count'] / total
    rawdata.loc[:, 'cumsum_ratio'] = rawdata.loc[:, 'count'].cumsum(axis=0) / total
    firstq = rawdata[rawdata['cumsum_ratio'] >= 0.25]['betamount'].iloc[0]
    median = rawdata[rawdata['cumsum_ratio'] >= 0.5]['betamount'].iloc[0]
    thridq = rawdata[rawdata['cumsum_ratio'] >= 0.75]['betamount'].iloc[0]
    q099 = rawdata[rawdata['cumsum_ratio'] >= 0.99]['betamount'].iloc[0]
    q0995 = rawdata[rawdata['cumsum_ratio'] >= 0.995]['betamount'].iloc[0]
    q0999 = rawdata[rawdata['cumsum_ratio'] >= 0.999]['betamount'].iloc[0]
    print('Mean of {} is {}'.format(gamedict[gameid], mean))
    print(
        'Quartile of {}: firstq={}, median={}, thirdq={}, 99%q={}, 99.5%q={}, 99.9%q={}'\
            .format(gamedict[gameid], firstq, median, thridq, q099, q0995, q0999))