# CC Fundamentals: Hypothesis Testing - 3
###################################################
######### Reference links #########
####################################################
import numpy as np
from scipy import stats
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
import pandas as pd

## Average hourly wage
# The average hourly wage of a sample of 150 workers in plant 'A' was Rs.2·87 with a standard deviation of Rs. 1·08.
# The average wage of a sample of 200 workers in plant 'B' was Rs. 2·56 with a standard deviation of Rs. 1·28.
# (i) Calculate the Z-score for this scenario.
# (ii) Can an applicant safely assume that the hourly wages paid by plant 'A' are higher than those paid by plant 'B' at a 1% significance level?
def TwoSampZTest(samp_mean_1, samp_mean_2, samp_std_1, samp_std_2, n1, n2):
  denominator = np.sqrt((samp_std_1**2 / n1) + (samp_std_2**2 / n2))
  z_score = (samp_mean_1 - samp_mean_2) / denominator
  return z_score
def hourly_wage():
  # Given data for plant A
  sample_mean_A = 2.87
  sample_std_A = 1.08
  sample_size_A = 150
  # Given data for plant B
  sample_mean_B = 2.56
  sample_std_B = 1.28
  sample_size_B = 200
  # Set the significance level
  significance_level = 0.01
  # Calculate the z-score using the function
  z_score = TwoSampZTest(sample_mean_A, sample_mean_B, sample_std_A, sample_std_B, sample_size_A, sample_size_B)
  # Calculate the one-tailed p-value
  p_value = 1-stats.norm.cdf(z_score)
  # Compare the p-value to the significance level
  if p_value < significance_level:
    conclusion = "Reject the null hypothesis. Hourly wages in plant 'A' are higher than those in plant 'B' at a 1% significance level."
  else:
    conclusion = "Fail to reject the null hypothesis. No significant difference in hourly wages between plant 'A' and 'B' at a 1% significance level."
  # Print the results
  print(f'z-score: {z_score:.4f}')
  print(f'p-value: {p_value:.4f}')
  print('Conclusion:', conclusion)

## Smokers
# When smokers smoke, nicotine is transformed into cotinine, which can be tested. The average cotinine level in a group of 50 smokers was 243.5 ng ml.
# Assuming that the standard deviation is known to be 229.5 ng ml. Test the assertion that the mean cotinine level of all smokers is equal to 300.0 ng ml, at 95% confidence.
## Answer - Null Hypothesis (H0): The mean cotinine level of all smokers is equal to 300.0 ng/ml. (µ = 300.0 ng)
# Alternative Hypothesis (Ha): The mean cotinine level of all smokers is not equal to 300.0 ng/ml. (µ ≠ 300.0 ng)
def smokers():
  # Given values
  sample_mean = 243.5  # Sample mean cotinine level
  population_std = 229.5  # Known population standard deviation
  population_mean = 300.0  # Hypothesized population mean
  sample_size = 50  # Sample size
  confidence_level = 0.95  # 95% confidence level
  # Calculate the Z-score
  standard_error = population_std / (sample_size**0.5)
  Z = (sample_mean - population_mean) / standard_error
  # Calculate the p-value for a two-tailed test
  p_value = 2 * (1 - stats.norm.cdf(abs(Z)))
  # Determine whether to reject the null hypothesis
  alpha = 1 - confidence_level
  if p_value < alpha:
    conclusion = "Reject the null hypothesis which means the mean cotinine level of all smokers is not equal to 300.0 ng/ml "
  else:
    conclusion = "Fail to reject the null hypothesis which means the mean cotinine level of all smokers is equal to 300.0 ng/ml. "
  print(f"Z-score: {Z}")
  print(f"P-value: {p_value}")
  print(f"Conclusion: {conclusion}")

## Institution's claim
# It is known that the mean IQ of high school students is 100, and the standard deviation is 15.
# A coaching institute claims that candidates who study there have more IQ than an average high school student. When the IQ of 50 candidates was calculated, the average turned out to be 110
# Conduct an appropriate hypothesis test to test the institute’s claim, with a significance level of 5%
## Answer - Null Hypothesis (H0): The average IQ of candidates from the institution is the same as the population's average IQ.(μ = 100)
# Alternative Hypothesis (Ha): The average IQ of candidates from the institution is higher than the population's average IQ.(μ > 100)
def institution():
  # Given values
  population_mean = 100
  population_std = 15
  sample_mean = 110
  sample_size = 50
  significance_level = 0.05
  # Calculate the standard error (standard deviation of the sample mean)
  standard_error = population_std / (sample_size**0.5)
  # Calculate the Z-score
  Z = (sample_mean - population_mean) / standard_error
  # Calculate the p-value for a one-tailed test
  p_value = 1 - stats.norm.cdf(Z)
  # Determine whether to reject the null hypothesis
  if p_value < significance_level:
    conclusion = "Reject the null hypothesis.Candidates who study at this coaching institution have more IQ than an average high school student."
  else:
    conclusion = "Fail to reject the null hypothesis. Candidates who study at this coaching institution have the same IQ as an average high school student."
  print(f"Z-score: {Z}")
  print(f"P-value: {p_value}")
  print(f"Conclusion: {conclusion}")

## Quality assurance
# The quality assurance department claims that on average the non-fat milk contains more than 190 mg of Calcium per 500 ml packet. To check this claim 45 packets of milk are collected and the content of calcium is recorded.
# Perform an appropriate test to check the claim with a 90% confidence level.
# data = [193, 321, 222, 158, 176, 149, 154, 223, 233, 177, 280, 244, 138, 210, 167, 129, 254, 167, 194, 191, 128, 191, 144, 184, 330, 216, 212, 142, 216, 197, 231, 133, 205, 192, 195, 243, 224, 137, 234, 171, 176, 249, 222, 234, 191]
# Note: Round off the answer to four decimal places.
## Answer - Since we need to test the claim made by company, we define our hypothesis as:
# H0: µ <= 190
# H1: µ > 190 (Right-tailed test)
# We perform one sample t-test.
def quality_assurance():
  data = pd.Series([193, 321, 222, 158, 176, 149, 154, 223, 233, 177, 280, 244, 138, 210, 167, 129, 254, 167, 194, 191, 128, 191, 144, 184, 330, 216, 212, 142, 216, 197, 231, 133, 205, 192, 195, 243, 224, 137, 234, 171, 176, 249, 222, 234, 191])
  print("Observed sample mean = ", round(data.mean(), 2))
  t_stat, p_value = ttest_1samp(data, popmean=190, alternative="greater")
  print("Test statistic = ", round(t_stat,4))
  print("P-value = ", round(p_value,4))
  if p_value < 0.10:
    print("Reject H0")
  else: 
    print("Fail to reject H0")

## Coaching class
# There are 8 females and 12 males in a coaching class. After a practice test, the coach wants to know whether the average score of females is greater than the average score of males.
# Given data describes the scores of females and males in his class. female_scores=[25,30,45,49,47,35,32,42], male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]
# Use an appropriate test to check whether the assumption of the coach is significant or not, at a 2% significance level?
## Answer - Based on the given problem, we define our hypothesis as:
# H0: μ1 ≤ μ2, i.e., the average score of females is not greater than the average score of males.
# H1: μ1 > μ2 i.e. the average score of females is greater than the average score of males.
# Based on these proposed hypothesis, we will need to perform Right-tailed test in order to test for the alternate hypothesis.
def coaching_class():
  female_scores=pd.Series([25,30,45,49,47,35,32,42])
  male_scores=pd.Series([45,47,25,22,29,32,27,28,40,49,50,33])
  t_stat, p_value = ttest_ind(female_scores, male_scores, alternative="greater")
  print("Test statistic = ", round(t_stat,3))
  print("P_value =",p_value )
  alpha=0.02
  if p_value < alpha:
    print("Reject the null hypothesis. There is significant evidence that the average score of females is greater than the average score of males.")
  else:
    print("Fail to reject the null hypothesis. There is no significant evidence that the average score of females is greater than the average score of males.")

  