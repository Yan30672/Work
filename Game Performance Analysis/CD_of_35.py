import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
requiredata = data[data.loc[:, "code"] == 35]
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
rawdata = requiredata.sort_values(by=['betamount']).dropna()
Total = rawdata['ct'].sum()
Average = (rawdata['betamount'] * rawdata['ct']).sum() / Total
Max = rawdata['betamount'].max()
Min = rawdata['betamount'].min()
rawdata.loc[:, 'ctratio'] = rawdata.loc[:, 'ct'] / Total
rawdata.loc[:, 'cumsum_ct'] = rawdata.loc[:, 'ctratio'].cumsum(axis=0)
Count = len(rawdata.index)

#partition
partition = [0.1, 0.6, 0.85, 0.94, 0.95, 0.98, 0.99, 1]
print(partition)
cumsum1 = rawdata[rawdata['cumsum_ct'] >= partition[0]]['betamount'].iloc[0]
cumsum2 = rawdata[rawdata['cumsum_ct'] >= partition[1]]['betamount'].iloc[0]
cumsum3 = rawdata[rawdata['cumsum_ct'] >= partition[2]]['betamount'].iloc[0]
cumsum4 = rawdata[rawdata['cumsum_ct'] >= partition[3]]['betamount'].iloc[0]
cumsum5 = rawdata[rawdata['cumsum_ct'] >= partition[4]]['betamount'].iloc[0]
cumsum6 = rawdata[rawdata['cumsum_ct'] >= partition[5]]['betamount'].iloc[0]
cumsum7 = rawdata[rawdata['cumsum_ct'] >= partition[6]]['betamount'].iloc[0]
cumsum8 = rawdata[rawdata['cumsum_ct'] >= partition[7]]['betamount'].iloc[0]
sep = [cumsum1, cumsum2, cumsum3, cumsum4, cumsum5, cumsum6, cumsum7, cumsum8]
print('Betamount切割點{}'.format(sep))

#plot 2D
fig, axes = plt.subplots(nrows=2, ncols=4)
plt.suptitle('Distribution of payoff conditioned on betamount of {}, where betamount has max = {}, min = {}, aver = {}'.format('GPk寶石糖果派對',Max,Min,Average), fontproperties=font)
cdf_betamount_cumsum1 = rawdata[rawdata['betamount'] <= cumsum1].sort_values(by=['payoff'])
len1 = len(cdf_betamount_cumsum1.index)
print(len1 / Count)
denom1 = cdf_betamount_cumsum1['ct'].sum()
cdf_betamount_cumsum1.loc[:, 'cumsum1_ct'] = cdf_betamount_cumsum1.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum1['con_cdf'] = cdf_betamount_cumsum1.apply(lambda row: row.cumsum1_ct / denom1, axis=1)
cdf_betamount_cumsum1.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[0, 0])
axes[0,0].set_xlabel('payoff')
axes[0,0].set_ylabel('probability')
axes[0,0].set_title('P(payoff|betamount<{})'.format(cumsum1), fontproperties=font)

cdf_betamount_cumsum2 = rawdata[rawdata['betamount'] <= cumsum2].sort_values(by=['payoff'])
denom2 = cdf_betamount_cumsum2['ct'].sum()
cdf_betamount_cumsum2.loc[:, 'cumsum2_ct'] = cdf_betamount_cumsum2.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum2['con_cdf'] = cdf_betamount_cumsum2.apply(lambda row: row.cumsum2_ct / denom2, axis=1)
cdf_betamount_cumsum2.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[0, 1])
axes[0,1].set_xlabel('payoff')
axes[0,1].set_ylabel('probability')
axes[0,1].set_title('P(payoff|betamount<{})'.format(cumsum2), fontproperties=font)

cdf_betamount_cumsum3 = rawdata[rawdata['betamount'] <= cumsum3].sort_values(by=['payoff'])
denom3 = cdf_betamount_cumsum3['ct'].sum()
cdf_betamount_cumsum3.loc[:, 'cumsum3_ct'] = cdf_betamount_cumsum3.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum3['con_cdf'] = cdf_betamount_cumsum3.apply(lambda row: row.cumsum3_ct / denom3, axis=1)
cdf_betamount_cumsum3.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[0, 2])
axes[0,2].set_xlabel('payoff')
axes[0,2].set_ylabel('probability')
axes[0,2].set_title('P(payoff|betamount<{})'.format(cumsum3), fontproperties=font)

cdf_betamount_cumsum4 = rawdata[rawdata['betamount'] <= cumsum4].sort_values(by=['payoff'])
denom4 = cdf_betamount_cumsum4['ct'].sum()
cdf_betamount_cumsum4.loc[:, 'cumsum4_ct'] = cdf_betamount_cumsum4.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum4['con_cdf'] = cdf_betamount_cumsum4.apply(lambda row: row.cumsum4_ct / denom4, axis=1)
cdf_betamount_cumsum4.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[0, 3])
axes[0,3].set_xlabel('payoff')
axes[0,3].set_ylabel('probability')
axes[0,3].set_title('P(payoff|betamount<{})'.format(cumsum4), fontproperties=font)

cdf_betamount_cumsum5 = rawdata[rawdata['betamount'] <= cumsum5].sort_values(by=['payoff'])
denom5 = cdf_betamount_cumsum5['ct'].sum()
cdf_betamount_cumsum5.loc[:, 'cumsum5_ct'] = cdf_betamount_cumsum5.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum5['con_cdf'] = cdf_betamount_cumsum5.apply(lambda row: row.cumsum5_ct / denom5, axis=1)
cdf_betamount_cumsum5.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[1, 0])
axes[1,0].set_xlabel('payoff')
axes[1,0].set_ylabel('probability')
axes[1,0].set_title('P(payoff|betamount<{})'.format(cumsum5), fontproperties=font)

cdf_betamount_cumsum6 = rawdata[rawdata['betamount'] <= cumsum6].sort_values(by=['payoff'])
denom6 = cdf_betamount_cumsum6['ct'].sum()
cdf_betamount_cumsum6.loc[:, 'cumsum6_ct'] = cdf_betamount_cumsum6.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum6['con_cdf'] = cdf_betamount_cumsum6.apply(lambda row: row.cumsum6_ct / denom6, axis=1)
cdf_betamount_cumsum6.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[1, 1])
axes[1,1].set_xlabel('payoff')
axes[1,1].set_ylabel('probability')
axes[1,1].set_title('P(payoff|betamount<{})'.format(cumsum6), fontproperties=font)

cdf_betamount_cumsum7 = rawdata[rawdata['betamount'] <= cumsum7].sort_values(by=['payoff'])
denom7 = cdf_betamount_cumsum7['ct'].sum()
cdf_betamount_cumsum7.loc[:, 'cumsum7_ct'] = cdf_betamount_cumsum7.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum7['con_cdf'] = cdf_betamount_cumsum7.apply(lambda row: row.cumsum7_ct / denom7, axis=1)
cdf_betamount_cumsum7.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[1, 2])
axes[1,2].set_xlabel('payoff')
axes[1,2].set_ylabel('probability')
axes[1,2].set_title('P(payoff|betamount<{})'.format(cumsum7), fontproperties=font)

cdf_betamount_cumsum8 = rawdata[rawdata['betamount'] <= cumsum8].sort_values(by=['payoff'])
denom8 = cdf_betamount_cumsum8['ct'].sum()
cdf_betamount_cumsum8.loc[:, 'cumsum8_ct'] = cdf_betamount_cumsum8.loc[:, 'ct'].cumsum(axis=0)
cdf_betamount_cumsum8['con_cdf'] = cdf_betamount_cumsum8.apply(lambda row: row.cumsum8_ct / denom8, axis=1)
cdf_betamount_cumsum8.plot(x='payoff', y='con_cdf', kind='scatter', ax=axes[1, 3])
axes[1,3].set_xlabel('payoff')
axes[1,3].set_ylabel('probability')
axes[1,3].set_title('P(payoff|betamount<{})'.format(cumsum8), fontproperties=font)

plt.show()