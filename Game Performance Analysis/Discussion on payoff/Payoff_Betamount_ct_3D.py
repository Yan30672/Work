import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
data = data.loc[data['payoff'] <= 5]
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

try:
    gameid = int(input('請輸入你要求的遊戲:'))
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    requiredata = data[data.loc[:, "code"] == gameid].dropna()
    fig = plt.figure()
    ax = Axes3D(fig)
    x = requiredata['betamount']
    y = requiredata['payoff']
    z = requiredata['ct']
    ax.scatter(x, y, z)
    plt.xlabel('betamount')
    plt.ylabel('payoff')
    plt.title('3D distribution of {}'.format(gamedict[gameid]), fontproperties=font)
    plt.show()
except IndexError:
    print('請輸入正確的gameid')