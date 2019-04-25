import numpy as np
from scipy import stats

mean1 = 350.459402
mean2 = 303.654095

std1 =  40.509514
std2 =  65.567013

nobs1 = 372
nobs2 = 239

modified_std1 = np.sqrt(np.float32(nobs1)/np.float32(nobs1-1)) * std1
modified_std2 = np.sqrt(np.float32(nobs2)/np.float32(nobs2-1)) * std2

(statistic, pvalue) = stats.ttest_ind_from_stats(mean1=mean1, std1=modified_std1, nobs1=372, mean2=mean2, std2=modified_std2, nobs2=239)

print("t statistic is: ", statistic)
print("pvalue is: ", pvalue)

t = (mean1 - mean2)*np.sqrt(nobs1*nobs2*(nobs1+nobs2-2)/(nobs1+nobs2)) / np.sqrt(nobs1*std1**2 + nobs2*std2**2)
print("t is: ", t)
print((1 - stats.t.cdf(t, nobs1+nobs2-2))*2)