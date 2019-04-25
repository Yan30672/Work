import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('Loyalty_Odds.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['JoinTime'] = pd.to_datetime(df['JoinTime'], format = '%Y-%m-%d %H:%M:%S.%f')
df['mtt'] = pd.to_datetime(df['mtt'], format = '%Y-%m-%d')
df['code'] = df[['rawdatatype', 'gametypeid']].apply(tuple, axis=1)
df['game'] = df['rawdata'] + df['gamename']
codec = [5901, 5902, 5908, 21, 35]
Dict = {(3,761):5902, (3,4356):5908, (3,760):5901, (89,7846):21, (89,8690):35}
df['Odds'] = df['Payoff'] / df['Betamount']

df['code'] = df['code'].map(Dict)
data = df[df['code'].isin(codec)]
data = data.drop(['rawdatatype', 'gametypeid', 'rawdata', 'gamename', 'game'], axis=1).sort_values(by = ['code', 'date', 'memberid'])

data.to_csv('data_Odds.csv', index=False)

print(data)
#
#data=['特定日期', '會員id', '特定日期的下注次數', '該會員的註冊時間', '該會員第一次遊玩的時間', '該會員在哪款遊戲下注']