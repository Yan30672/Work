import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_csv("loyaldata3m.csv")
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
fig, axes = plt.subplots(nrows=2, ncols=3)

rawdata1 = df[df['code'] == 5901].sort_values(by = ['memberid'])
print(rawdata1['loyalty'].describe())
rawdata1.hist(column='loyalty', ax = axes[0,0])
axes[0,0].set_xlabel('loyalty')
axes[0,0].set_ylabel('counts')
axes[0,0].set_title('Histogram of loyalty of {}'.format(gamedict[5901]), fontproperties=font)

rawdata2 = df[df['code'] == 5902].sort_values(by = ['memberid'])
print(rawdata2['loyalty'].describe())
rawdata2.hist(column='loyalty', ax = axes[0,1])
axes[0,1].set_xlabel('loyalty')
axes[0,1].set_ylabel('counts')
axes[0,1].set_title('Histogram of loyalty of {}'.format(gamedict[5902]), fontproperties=font)

rawdata3 = df[df['code'] == 5908].sort_values(by = ['memberid'])
print(rawdata3['loyalty'].describe())
rawdata3.hist(column='loyalty', ax = axes[0,2])
axes[0,2].set_xlabel('loyalty')
axes[0,2].set_ylabel('counts')
axes[0,2].set_title('Histogram of loyalty of {}'.format(gamedict[5908]), fontproperties=font)

rawdata4 = df[df['code'] == 21].sort_values(by = ['memberid'])
print(rawdata4['loyalty'].describe())
rawdata4.hist(column='loyalty', ax = axes[1,0])
axes[1,0].set_xlabel('loyalty')
axes[1,0].set_ylabel('counts')
axes[1,0].set_title('Histogram of loyalty of {}'.format(gamedict[21]), fontproperties=font)

rawdata5 = df[df['code'] == 35].sort_values(by = ['memberid'])
print(rawdata5['loyalty'].describe())
rawdata5.hist(column='loyalty', ax = axes[1,1])
axes[1,1].set_xlabel('loyalty')
axes[1,1].set_ylabel('counts')
axes[1,1].set_title('Histogram of loyalty of {}'.format(gamedict[35]), fontproperties=font)

plt.show()

