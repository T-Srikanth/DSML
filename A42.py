# CC Fundamentals: Hypothesis Testing - 2
###################################################
######### Reference links #########
####################################################

## Pastries produced per day
# A French cafe has historically maintained that their average daily pastry production is at most 500.
# With the installation of a new machine, they assert that the average daily pastry production has increased. The average number of pastries produced per day over a 70-day period was found to be 530.
# Assume that the population standard deviation for the pastries produced per day is 125.
# Perform a z-test with the critical z-value = 1.64 at the alpha (significance level) = 0.05 to evaluate if there's sufficient evidence to support their claim of the new machine producing more than 500 pastries daily.
# Note: Round off the z-score to two decimal places.
# Import necessary library
import scipy.stats as stats
import numpy as np
import math
# Define sample mean, standard deviation, and sample size
def z_test():
  sample_mean = 530
  population_std = 125
  sample_size = 70
  population_mean = 500
  # Calculate z-score
  z_score = (sample_mean - population_mean) / (population_std / np.sqrt(sample_size))
  # Round z-score to two decimal places
  z_score = round(z_score, 2)
  print(f"z-score: {z_score}")
  # Set critical z-value and confidence level
  confidence_level = 0.95
  critical_z = stats.norm.ppf(confidence_level)
  print("critical z-value:",critical_z)
  # Check if the z-score is greater than the critical z-value
  if z_score > critical_z:
    print("Reject the null hypothesis. The shop's claim is supported by the data.")
  else:
    print("Fail to reject the null hypothesis. There is not enough evidence to support the shop's claim.")

## Water Regulation
# The student hostel office at IIT Madras estimates that each student uses more than 3.5 buckets of water per day.
# In order to verify this claim, the college trustees decide to monitor the water consuption over the next 45 days, and it is found that on an average, 3.72 buckets of water is consumed by a student, per day.
# Assume that the population standard deviation is 0.7 buckets. What is the critical sample mean, assuming a critical z-value of 1.28?
# Note: The critical sample mean is defined as the mean value for which the z-score is equal to the critical value. Also, round off the final answer to three decimal places.

def water_regulation():
  # Given values
  population_mean = 3.5
  population_std = 0.7
  critical_z_value = 1.28
  sample_size = 45
  # Calculate the critical sample mean
  critical_sample_mean = population_mean + (critical_z_value * (population_std / math.sqrt(sample_size)))
  # Round off the answer to three decimal places
  critical_sample_mean = round(critical_sample_mean, 3)
  print("Critical Sample Mean:", critical_sample_mean)

## India Runs on Chai
# The Chai Point stall at Bengaluru airport estimates that each person visiting the store drinks an average of 1.7 small cups of tea.
# Assume a population standard deviation of 0.5 small cups. A sample of 30 customers collected over a few days averaged 1.85 small cups of tea per person.
# Test the claim using an appropriate test at an alpha = 0.05 significance value, with a critical z-score value of ±1.96.
# Note: Round off the z-score to two decimal places.
def chai_point():
  # Define sample mean, standard deviation, and sample size
  sample_mean = 1.85
  population_std = 0.5
  sample_size = 30
  population_mean = 1.7
  # Calculate z-score
  z_score = (sample_mean - population_mean) / (population_std / np.sqrt(sample_size))
  # Round z-score to two decimal places
  z_score = np.round(z_score, 2)
  # Set alpha and critical z-score (use two-tailed since direction is unknown)
  alpha = 0.05
  critical_z = 1.96
  # Check if the z-score is greater than the critical z-value
  if abs(z_score) > critical_z:
    print(f"z-score: {z_score}")
    print("Reject the null hypothesis. The average tea consumption is likely different from the estimate.")
  else:
    print(f"z-score: {z_score}")
    print("Fail to reject the null hypothesis. There is not enough evidence to support a difference from the estimated average.")