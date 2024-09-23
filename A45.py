# CC Fundamentals: Correlation Test
###################################################
######### Reference links #########
####################################################

from scipy.stats import ttest_rel
import numpy as np
## Zumba trainer
# The Zumba trainer claims to the customers, that their new dance routine helps to reduce more weight. Weight of 8 people were recorded before and after following the new Zumba training for a month:
# wt_before = [85, 74, 63.5, 69.4, 71.6, 65,90,78]
# wt_after = [82, 71, 64, 65.2, 67.8, 64.7,95,77]
# Test the trainer's claim with 90% confidence. Further, what would be the pvalue?
def zumba():
  # H0: Customers did not reduce their weight after 1 month of new Zumba routine μ_Before = μ_After
  # ​H1: Customers have reduced their weight after 1 month of new Zumba routine μ_Before > μ_After
  # Given samples of weight before and after 1 month of following new Zumba routine
  wt_before = [85, 74, 63.5, 69.4, 71.6, 65,90,78]
  wt_after = [82, 71, 64, 65.2, 67.8, 64.7,95,77]
  alpha = 0.10 # Significance level
  # Performing Paired Right-Tailed T-test
  t_stat, pvalue = ttest_rel(wt_before, wt_after, alternative="greater" )
  print('Test Statistic:', t_stat)
  print('P value:', pvalue)
  if pvalue < alpha:
    print('Reject H0 ; Customers have reduced their weight after 1 month of new Zumba routine')
  else:
    print('Fail to reject H0 ; Customers did not reduce their weight after 1 month of new Zumba routine')

## Test the Training Program
# You are appointed as a Data Analyst for a training program deployed by the Government of India.
# The participants’ skills were tested before and after the training using some metrics on a scale of 10.
# before = [2.45, 0.69, 1.80, 2.80, 0.07, 1.67, 2.93, 0.47, 1.45, 1.34]   
# after = [7.71, 2.17, 5.65, 8.79, 0.23, 5.23, 9.19, 1.49, 4.56, 4.20] 
# Conduct an appropriate test to assess a statistically significant increase in the average skill score after the training program, and then answer the below questions accordingly.
# Note: Perform the test at alpha = 5%.
def training_program():
  # H0: No improvement in skills after training, i.e. μ_1 = μ_2
  # ​Ha: Positive effect / improvement in skills after training, i.e. μ_1 < μ_2​	
# Sample of participants’ skills tested before and after the training
  before= [2.45, 0.69, 1.80, 2.80, 0.07, 1.67, 2.93, 0.47, 1.45, 1.34]
  after = [7.71, 2.17, 5.65, 8.79, 0.23, 5.23, 9.19, 1.49, 4.56, 4.20]
  before_mean = np.mean(np.array(before))
  after_mean = np.mean(np.array(after))
  print("before mean:",before_mean)
  print("after mean:",after_mean)
  # Performing the paired t-test
  t_obs, p = ttest_rel(before, after, alternative="less")
  print(" T statistic = ", round(t_obs,2))
  print(" p-value = ", round(p,4))
  if(p < 0.05):
    print("Since, p-value < alpha, we reject the null hypothesis. Positive effect / improvement in skills after training")
  else:
    print("Since, p-value > alpha, we fail to reject the null hypothesis. No effect / improvement in skills after training")