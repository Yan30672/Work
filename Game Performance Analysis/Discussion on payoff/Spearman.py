import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

for gameid in [5901, 5902, 5908, 21, 35]:
    rawdata = data[data.loc[:, "code"] == gameid].dropna().drop(columns=['code'])
    n = rawdata['ct'].sum()
    betamount1 = rawdata.groupby('betamount')['ct'].sum().reset_index(name = 'ct').sort_values(by = ['ct'], ascending=False)
    betamount1['ranked'] = betamount1['ct'].cumsum() - (betamount1['ct']-1)/2
    dict1 = dict(zip(betamount1.betamount, betamount1.ranked))
    payoff1 = rawdata.groupby('payoff')['ct'].sum().reset_index(name = 'ct').sort_values(by = ['ct'], ascending=False)
    payoff1['ranked'] = payoff1['ct'].cumsum() - (payoff1['ct']-1)/2
    dict2 = dict(zip(payoff1.payoff, payoff1.ranked))
    rawdata['betamount_ranks'] = rawdata['betamount'].map(dict1)
    rawdata['payoff_ranks'] = rawdata['payoff'].map(dict2)
    rawdata['dsquare'] = (rawdata['betamount_ranks'] - rawdata['payoff_ranks']) ** 2
    sums = rawdata['dsquare'].sum()
    a = sums / (n-1)
    b = a / n
    c = b / (n+1)
    spearman = 1- 6 * c
    print('The spearman correlation between payoff and betamount of {} is {}'.format(gamedict[gameid],spearman))