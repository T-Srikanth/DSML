# DSML Adv: CLT, Confidence intervals
###################################################
######### Reference links #########
####################################################

# Confidence Interval list
# Given a sample of data in a Python list, calculate the 68%, 95%, and 99% confidence interval of its mean using the Z-multiplier. The Z-multiplier for 68%, 95%, and 99% is 1, 1.96, and 2.57 respectively.
# The output must be a list of lists with each internal list containing the required confidence interval in the order of 68%, 95%, and 99%.
import numpy as np
def ciList(data):
  '''
  input: data -> Variable containing the input data in form of python list
  output: res -> A list of list variable with each internal list containing the required confidence interval in the order of 68%, 95%, and 99%
  '''
  # Z-multipliers for 68%, 95%, and 99% confidence levels
  z_multipliers = [1, 1.96, 2.57]
  res = [[np.round(np.mean(data) - (i * (np.std(data) / np.sqrt(len(data)))),2), np.round(np.mean(data) + (i * (np.std(data) / np.sqrt(len(data)))),2)] for i in z_multipliers]
  return res
sample = [2, 3, 5, 6, 7, 9, 8, 1, 2]
# print(ciList(sample))

## Tip percentage
# The tip percentage for a delivery person has a mean value of 28% and a standard deviation of 7%.
# What is the probability that the sample mean tip percentage for a random sample of 50 bills is between 26% and 31%?
from scipy.stats import norm
def prob(u1=31,u2=26,n=50,u=28,sd=7):
  return (norm.cdf((u1-u)/(sd/np.sqrt(n))) - norm.cdf((u2-u)/(sd/np.sqrt(n)))).round(3)
# print(prob())

## Led lights
# The life of LED light bulbs manufactured in a factory is normally distributed with a mean equal to 900 hours and a standard deviation of 50 hours.
# Find the probability that a random sample of 20 bulbs will have an average life of less than 875 hours. (Round off the answer to 4 decimal points)
def prob_avg_life():
  sigma = 50
  n = 20
  sample_mean = 900
  x = 875
  # std deviation  sigma/sqrt(n)
  std_error = sigma/np.sqrt(n)
  z = (x-sample_mean)/std_error
  prob = norm.cdf(z)
  return round(prob,4)