# CC Fundamentals: ANOVA
###################################################
######### Reference links #########
####################################################

import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2
from scipy.stats import chisquare
from scipy.stats import f_oneway

## Is education gender independent?
# A random sample of 395 people was surveyed and each person was asked to report the highest education level they obtained. The data observed are summarized below:
# Female(60, 54, 46, 41, 201), Male(40, 44, 53, 57, 194) and Total(100, 98, 99, 98, 395), where variables in each class are (High school, Bachelors, Masters, Ph.d, Total).
# The expected values are: Female(50.866, 49.868, 50.377, 49.868, 201), Male(49.114, 48.132, 48.623, 48.132, 194) and Total(100, 98, 99, 98, 395). Are gender and education levels dependent at a 5% significance level?
## Answer - H0: the variables are independent.(i.e. education level and gender)
# H1: the variables are dependent.
def chi_test():
  Female = [60, 54, 46, 41]
  Male = [40, 44, 53, 57]
  array = np.array([Female,Male])
  #performing chi2 test
  chi_stat, p, dof, expected = chi2_contingency(observed = array, correction = False)
  print("Test statistic:", chi_stat)
  print("p-value:", p)
  print("Degrees of freedom:", dof)
  chi2_val = np.abs(round(stats.chi2.isf(q = 0.05, df = 3), 4))
  print('Critical value for chi-square test:', chi2_val)
  if chi_stat < chi2_val:
    print("Chi statistic  < Chi critical. So, fail to reject null hypothesis")
  else:
    print("Chi statistic  > Chi critical. So, reject null hypothesis")

## Observation representing sample
# According to a survey conducted on car owners, it was determined that
#   - 60% of owners have only one car,
#   - 28% have two cars, and
#   - 12% have three or more cars.
# Suppose Ram conducted his own survey within his residential society, and found that
#   - 73 owners have only one car,
#   - 38 owners have two cars, and
#   - 18 owners have three or more cars.
# Determine whether Ram's survey supports the original one, with a significance level of 0.05.
##Answer Null Hypothesis (H0): The distribution of the number of cars owned by car owners in your survey is the same as the distribution in the original survey.
# Alternative Hypothesis (H1): The distribution of the number of cars owned by car owners in your survey is different from the distribution in the original survey.
def chisquare_test():
  # Original survey distribution
  expected_distribution = np.array([0.60, 0.28, 0.12])
  # Your survey results
  observed_distribution = np.array([73, 38, 18])
  # Calculate the expected counts based on your sample size
  total_sample_size = observed_distribution.sum()
  expected_counts = expected_distribution * total_sample_size
  # Perform the Chi-Square Goodness of Fit test
  chi_squared_stat, p_value = chisquare(f_obs=observed_distribution, f_exp=expected_counts)
  # Define the significance level (alpha)
  alpha = 0.05
  # Check if the p-value is less than alpha to determine significance
  if p_value < alpha:
    print("Reject the null hypothesis. Your survey results are significantly different.")
  else:
    print("Fail to reject the null hypothesis. Your survey results are consistent with the original survey.")
  print(f"Chi-Square Statistic: {chi_squared_stat}")
  print(f"P-value: {p_value}")

## Four machines
# Suppose there a four machines m1, m2, m3, and m4 in a factory that is used to produce a certain kind of cotton fabric.
# Samples of size 4 with each unit having 100sq. meters are selected from the output of the machine randomly, and the number of flaws in every 100 sq. meters is counted and listed below.
# m1 = [8, 9, 11, 12]
# m2 = [6, 8, 10, 4]
# m3 = [14, 12, 18, 9]
# m4 = [20, 22, 25, 23]
# Do you think there is a significant difference in the performance of the four machines?
# Check whether there is a significant difference (consider a 5% significance level)
## Answer Null Hypothesis (H0): The means of flaws in the fabric produced by all four machines are equal.
# Alternative Hypothesis (Ha): At least one of the machine means is different from the others.
def four_machines():
  m1 = np.array([8, 9, 11, 12])
  m2 = np.array([6, 8, 10, 4])
  m3 = np.array([14, 12, 18, 9])
  m4 = np.array([20, 22, 25, 23])
  # Perform one-way ANOVA
  f_statistic, p_value = f_oneway(m1, m2, m3, m4)
  # Significance level (alpha)
  alpha = 0.05
  print("F-statistic:", f_statistic)
  print("p-value:", p_value)
  # Compare p-value with significance level
  if p_value < alpha:
    print("Reject null hypothesis: There is a significant difference in machine performance.")
  else:
    print("Fail to reject null hypothesis: There is no significant difference in machine performance.")

## Three sales persons
# A Company wishes to test whether three sales persons Saurav, Naveen, and Radha make the same sales or they differ in their selling ability by comparing the average number of sales made by them last week.
# Out of 14 sales 'Saurav' made 5, 'Naveen' made 4 and 'Radha' made 5. The following arrays describes the records of the sales persons in rupees.
# Saurav = [300, 400, 300, 500, 50]
# Naveen = [600, 300, 300, 400]
# Radha = [700, 300, 400, 600, 500]
# Test whether the average sales of the Saurav, Naveen, and Radha differ in size at a 95% confidence level.
'''
Null Hypothesis (H0): The average sales of Saurav, Naveen, and Radha are equal.
Alternative Hypothesis (Ha): At least one of the salesperson's average sales is different from the others.'''
def three_sales_persons():
  saurav = np.array([300, 400, 300, 500, 50])
  naveen = np.array([600, 300, 300, 400])
  radha = np.array([700, 300, 400, 600, 500])
  # Perform one-way ANOVA
  f_statistic, p_value = f_oneway(saurav, naveen, radha)
  # Significance level (alpha)
  alpha = 0.05
  print("F-statistic:", f_statistic)
  print("p-value:", p_value)
  # Compare p-value with significance level
  if p_value < alpha:
    print("Reject null hypothesis: There is a significant difference in average sales.")
  else:
    print("Fail to reject null hypothesis: There is no significant difference in average sales.")