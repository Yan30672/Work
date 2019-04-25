import pandas as pd
import datetime

pd.set_option('display.max_columns', None)
df = pd.read_csv('data_Odds.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['JoinTime'] = pd.to_datetime(df['JoinTime'], format = '%Y-%m-%d %H:%M:%S.%f')
df['mtt'] = pd.to_datetime(df['mtt'], format = '%Y-%m-%d')
df['code'] = df['code'].astype(int)

print(df)

gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}

online = []
for game in [5901, 5902, 5908, 21, 35]:
    rawdata = df[df['code'] == game].sort_values(by = ['date', 'memberid'])
    memberlist = rawdata.memberid.unique().tolist()
    for member in memberlist:
        memberdata = rawdata[rawdata['memberid'] == member]
        max = memberdata.date.max()
        d = datetime.timedelta(days = 89)
        min = max - d
        memberdata = memberdata[(memberdata['date'] >= min) & (memberdata['date'] <= max) ]
        onlinefreq = memberdata.shape[0]
        memberdata['Odds'] = memberdata['Payoff'] / memberdata['Betamount']
        wins = memberdata[memberdata['Odds'] > 0].shape[0] / onlinefreq
        online.append((member, onlinefreq, game, wins))
loyaldata = pd.DataFrame(online, columns=['memberid', 'onlinefreq', 'code', 'wins'])
loyaldata['loyalty'] = loyaldata['onlinefreq'] / 90
loyaldata.to_csv('loyaldata3m_Wins.csv', index=False)