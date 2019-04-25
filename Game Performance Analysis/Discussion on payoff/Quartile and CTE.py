import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math

pd.set_option('display.max_columns', None)
df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
# 資料整理
rawdata1 = data[data.loc[:, "code"] == 5901].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
total1 = rawdata1['count'].sum()
rawdata1.loc[:, 'ratio'] = rawdata1.loc[:, 'count']/total1
rawdata1.loc[:, 'cumsum_ratio'] = rawdata1.loc[:, 'count'].cumsum(axis=0) / total1
rawdata2 = data[data.loc[:, "code"] == 5902].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
total2 = rawdata2['count'].sum()
rawdata2.loc[:, 'ratio'] = rawdata2.loc[:, 'count']/total2
rawdata2.loc[:, 'cumsum_ratio'] = rawdata2.loc[:, 'count'].cumsum(axis=0) / total2
rawdata3 = data[data.loc[:, "code"] == 5908].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
total3 = rawdata3['count'].sum()
rawdata3.loc[:, 'ratio'] = rawdata3.loc[:, 'count']/total3
rawdata3.loc[:, 'cumsum_ratio'] = rawdata3.loc[:, 'count'].cumsum(axis=0) / total3
rawdata4 = data[data.loc[:, "code"] == 21].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
total4 = rawdata4['count'].sum()
rawdata4.loc[:, 'ratio'] = rawdata4.loc[:, 'count']/total4
rawdata4.loc[:, 'cumsum_ratio'] = rawdata4.loc[:, 'count'].cumsum(axis=0) / total4
rawdata5 = data[data.loc[:, "code"] == 35].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
total5 = rawdata5['count'].sum()
rawdata5.loc[:, 'ratio'] = rawdata5.loc[:, 'count']/total5
rawdata5.loc[:, 'cumsum_ratio'] = rawdata5.loc[:, 'count'].cumsum(axis=0) / total5

# 資料特徵
firstq1 = rawdata1[rawdata1['cumsum_ratio'] >= 0.25]['payoff'].iloc[0]
median1 = rawdata1[rawdata1['cumsum_ratio'] >= 0.5]['payoff'].iloc[0]
thridq1 = rawdata1[rawdata1['cumsum_ratio'] >= 0.75]['payoff'].iloc[0]
q099_1 = rawdata1[rawdata1['cumsum_ratio'] >= 0.99]['payoff'].iloc[0]
q0995_1 = rawdata1[rawdata1['cumsum_ratio'] >= 0.995]['payoff'].iloc[0]
q0999_1 = rawdata1[rawdata1['cumsum_ratio'] >= 0.999]['payoff'].iloc[0]

firstq2 = rawdata2[rawdata2['cumsum_ratio'] >= 0.25]['payoff'].iloc[0]
median2 = rawdata2[rawdata2['cumsum_ratio'] >= 0.5]['payoff'].iloc[0]
thridq2 = rawdata2[rawdata2['cumsum_ratio'] >= 0.75]['payoff'].iloc[0]
q099_2 = rawdata2[rawdata2['cumsum_ratio'] >= 0.99]['payoff'].iloc[0]
q0995_2 = rawdata2[rawdata2['cumsum_ratio'] >= 0.995]['payoff'].iloc[0]
q0999_2 = rawdata2[rawdata2['cumsum_ratio'] >= 0.999]['payoff'].iloc[0]

firstq3 = rawdata3[rawdata3['cumsum_ratio'] >= 0.25]['payoff'].iloc[0]
median3 = rawdata3[rawdata3['cumsum_ratio'] >= 0.5]['payoff'].iloc[0]
thridq3 = rawdata3[rawdata3['cumsum_ratio'] >= 0.75]['payoff'].iloc[0]
q099_3 = rawdata3[rawdata3['cumsum_ratio'] >= 0.99]['payoff'].iloc[0]
q0995_3 = rawdata3[rawdata3['cumsum_ratio'] >= 0.995]['payoff'].iloc[0]
q0999_3 = rawdata3[rawdata3['cumsum_ratio'] >= 0.999]['payoff'].iloc[0]

firstq4 = rawdata4[rawdata4['cumsum_ratio'] >= 0.25]['payoff'].iloc[0]
median4 = rawdata4[rawdata4['cumsum_ratio'] >= 0.5]['payoff'].iloc[0]
thridq4 = rawdata4[rawdata4['cumsum_ratio'] >= 0.75]['payoff'].iloc[0]
q099_4 = rawdata4[rawdata4['cumsum_ratio'] >= 0.99]['payoff'].iloc[0]
q0995_4 = rawdata4[rawdata4['cumsum_ratio'] >= 0.995]['payoff'].iloc[0]
q0999_4 = rawdata4[rawdata4['cumsum_ratio'] >= 0.999]['payoff'].iloc[0]

firstq5 = rawdata5[rawdata5['cumsum_ratio'] >= 0.25]['payoff'].iloc[0]
median5 = rawdata5[rawdata5['cumsum_ratio'] >= 0.5]['payoff'].iloc[0]
thridq5 = rawdata5[rawdata5['cumsum_ratio'] >= 0.75]['payoff'].iloc[0]
q099_5 = rawdata5[rawdata5['cumsum_ratio'] >= 0.99]['payoff'].iloc[0]
q0995_5 = rawdata5[rawdata5['cumsum_ratio'] >= 0.995]['payoff'].iloc[0]
q0999_5 = rawdata5[rawdata5['cumsum_ratio'] >= 0.999]['payoff'].iloc[0]

print('Quartile of {}: firstq={}, median={}, thirdq={}, 99%q={}, 99.5%q={}, 99.9%q={}'.format(gamedict[5901], firstq1, median1, thridq1, q099_1, q0995_1, q0999_1))
print('Quartile of {}: firstq={}, median={}, thirdq={}, 99%q={}, 99.5%q={}, 99.9%q={}'.format(gamedict[5902], firstq2, median2, thridq2, q099_2, q0995_2, q0999_2))
print('Quartile of {}: firstq={}, median={}, thirdq={}, 99%q={}, 99.5%q={}, 99.9%q={}'.format(gamedict[5908], firstq3, median3, thridq3, q099_3, q0995_3, q0999_3))
print('Quartile of {}: firstq={}, median={}, thirdq={}, 99%q={}, 99.5%q={}, 99.9%q={}'.format(gamedict[21], firstq4, median4, thridq4, q099_4, q0995_4, q0999_4))
print('Quartile of {}: firstq={}, median={}, thirdq={}, 99%q={}, 99.5%q={}, 99.9%q={}'.format(gamedict[35], firstq5, median5, thridq5, q099_5, q0995_5, q0999_5))

#P(payoff>num) and E(payoff|paypff>num)

rawdata1.loc[:, 'tail'] = 1 - rawdata1['cumsum_ratio'] + rawdata1['ratio']
rawdata1.loc[:, 'expectation'] = rawdata1['payoff'] * rawdata1['ratio']
rawdata1.loc[:, 'cumsum_exp'] = rawdata1['expectation'].cumsum()
total_expectation1 = rawdata1['expectation'].sum()
rawdata1.loc[:, 'tail_exp'] = total_expectation1 - rawdata1['cumsum_exp'] + rawdata1['expectation']
rawdata1.loc[:, 'CTE'] = rawdata1['tail_exp'] / rawdata1['tail']
rawdata1['log_payoff'] = rawdata1.apply(lambda row: math.log(2 + row.payoff), axis = 1)
rawdata1['log_CTE'] = rawdata1.apply(lambda row: math.log(1 + row.CTE), axis = 1)

rawdata2.loc[:, 'tail'] = 1 - rawdata2['cumsum_ratio'] + rawdata2['ratio']
rawdata2.loc[:, 'expectation'] = rawdata2['payoff'] * rawdata2['ratio']
rawdata2.loc[:, 'cumsum_exp'] = rawdata2['expectation'].cumsum()
total_expectation2 = rawdata2['expectation'].sum()
rawdata2.loc[:, 'tail_exp'] = total_expectation2 - rawdata2['cumsum_exp'] + rawdata2['expectation']
rawdata2.loc[:, 'CTE'] = rawdata2['tail_exp'] / rawdata2['tail']
rawdata2['log_payoff'] = rawdata2.apply(lambda row: math.log(2 + row.payoff), axis = 1)
rawdata2['log_CTE'] = rawdata2.apply(lambda row: math.log(1 + row.CTE), axis = 1)

rawdata3.loc[:, 'tail'] = 1 - rawdata3['cumsum_ratio'] + rawdata3['ratio']
rawdata3.loc[:, 'expectation'] = rawdata3['payoff'] * rawdata3['ratio']
rawdata3.loc[:, 'cumsum_exp'] = rawdata3['expectation'].cumsum()
total_expectation3 = rawdata3['expectation'].sum()
rawdata3.loc[:, 'tail_exp'] = total_expectation3 - rawdata3['cumsum_exp'] + rawdata3['expectation']
rawdata3.loc[:, 'CTE'] = rawdata3['tail_exp'] / rawdata3['tail']
rawdata3['log_payoff'] = rawdata3.apply(lambda row: math.log(2 + row.payoff), axis = 1)
rawdata3['log_CTE'] = rawdata3.apply(lambda row: math.log(1 + row.CTE), axis = 1)

rawdata4.loc[:, 'tail'] = 1 - rawdata4['cumsum_ratio'] + rawdata4['ratio']
rawdata4.loc[:, 'expectation'] = rawdata4['payoff'] * rawdata4['ratio']
rawdata4.loc[:, 'cumsum_exp'] = rawdata4['expectation'].cumsum()
total_expectation4 = rawdata4['expectation'].sum()
rawdata4.loc[:, 'tail_exp'] = total_expectation4 - rawdata4['cumsum_exp'] + rawdata4['expectation']
rawdata4.loc[:, 'CTE'] = rawdata4['tail_exp'] / rawdata4['tail']
rawdata4['log_payoff'] = rawdata4.apply(lambda row: math.log(2 + row.payoff), axis = 1)
rawdata4['log_CTE'] = rawdata4.apply(lambda row: math.log(1 + row.CTE), axis = 1)

rawdata5.loc[:, 'tail'] = 1 - rawdata5['cumsum_ratio'] + rawdata5['ratio']
rawdata5.loc[:, 'expectation'] = rawdata5['payoff'] * rawdata5['ratio']
rawdata5.loc[:, 'cumsum_exp'] = rawdata5['expectation'].cumsum()
total_expectation5 = rawdata5['expectation'].sum()
rawdata5.loc[:, 'tail_exp'] = total_expectation5 - rawdata5['cumsum_exp'] + rawdata5['expectation']
rawdata5.loc[:, 'CTE'] = rawdata5['tail_exp'] / rawdata5['tail']
rawdata5['log_payoff'] = rawdata5.apply(lambda row: math.log(2 + row.payoff), axis = 1)
rawdata5['log_CTE'] = rawdata5.apply(lambda row: math.log(1 + row.CTE), axis = 1)

#plot
fig, axes = plt.subplots(nrows=2, ncols=3)
plt.suptitle('Conditional tail expectation')

rawdata1.plot(x='log_payoff', y='log_CTE', kind='line', ax=axes[0,0])
axes[0,0].set_xlabel('ln(2+payoff)')
axes[0,0].set_ylabel('ln(1+CTE)')
axes[0,0].set_title('CTE of {}'.format(gamedict[5901]), fontproperties=font)

rawdata2.plot(x='log_payoff', y='log_CTE', kind='line', ax=axes[0,1])
axes[0,1].set_xlabel('ln(2+payoff)')
axes[0,1].set_ylabel('ln(1+CTE)')
axes[0,1].set_title('CTE of {}'.format(gamedict[5902]), fontproperties=font)

rawdata3.plot(x='log_payoff', y='log_CTE', kind='line', ax=axes[0,2])
axes[0,2].set_xlabel('ln(2+payoff)')
axes[0,2].set_ylabel('ln(1+CTE)')
axes[0,2].set_title('CTE of {}'.format(gamedict[5908]), fontproperties=font)

rawdata4.plot(x='log_payoff', y='log_CTE', kind='line', ax=axes[1,0])
axes[1,0].set_xlabel('ln(2+payoff)')
axes[1,0].set_ylabel('ln(1+CTE)')
axes[1,0].set_title('CTE of {}'.format(gamedict[21]), fontproperties=font)

rawdata5.plot(x='log_payoff', y='log_CTE', kind='line', ax=axes[1,1])
axes[1,1].set_xlabel('ln(2+payoff)')
axes[1,1].set_ylabel('ln(1+CTE)')
axes[1,1].set_title('CTE of {}'.format(gamedict[35]), fontproperties=font)

plt.show()
