# CLT and COnfidence Interval
###################################################
######### Reference links #########
####################################################

## Tip percentage
# The tip percentage for a delivery person has a mean value of 28% and a standard deviation of 7%.
# What is the probability that the sample mean tip percentage for a random sample of 50 bills is between 26% and 31%?
from scipy.stats import norm
import numpy as np
# expectation of sample mean would be same as population mean = 28% and sample standard deviation would be: population standard deiavtion/sqrt(no. of samples) > sigma/sqrt(n)
def tip():
  res = norm.cdf((31-28)/(7/np.sqrt(50))) - norm.cdf((26-28)/(7/np.sqrt(50)))
  return res
  
## No errors
# The first assessment in a statistical class involves computing a short program. If past experience indicates that 30% of all students will make no errors in the program, 
# use an appropriate normal approximation to compute the probability that in a class of 70 students, at least 28 will make no errors.
## Answer:
# Let X = the number of students out of 70 whose programs contain no errors.
# Then X ~ Bin(70, 0.3)
# The Central Limit Theorem implies that X is approximately normal with mean µ = np = 70 x 0.3 = 21 and
# standard deviation σ = √( npq ) = √( 70 x 0.3 x 0.7 ) = 3.834
# The probability that in a class of 70 students at least 28 will make no errors is:
# P(X ≥ 28) = 1 - P(X < 28) = 1 - P(Z < (28-21)/3.834) = 0.03394
def no_error():
  mean = 70*0.3
  sigma = np.sqrt(70*0.3*0.7)
  return 1 - norm.cdf((28-mean)/sigma)
# print(no_error())