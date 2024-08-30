# DSML Advanced: Probability Distributions - 3
###################################################
######### Reference links #########
####################################################

## IQR outlier detection
# Outliers are certain points in the data set which deviate from the general trends in the dataset. There are several ways to detect outliers. In this problem, we will use the median absolute deviation method to find outliers. According to this method:
#  - Find the Inter-quartile range [Q3 - Q1]
#  - Upper range is computed as Q3 + 1.5*IQR
#  - Lower range is computed as Q1 - 1.5*IQR
#  - Values that have high values than upper range are suspected to be outliers.
#  - Values that have low values than lower range are suspected to be outliers.
# Complete the function that identifies the outliers and return them by applying the function on the input list. In case no outliers are present, return an empty list.
import numpy as np
def outlier(data):
  '''
  Input:
  data: input data in the form of a python list
  Output:
  ans: return the list of outliers in the form of a python list. If no outliers are present, return an empty list
  '''
  q75, q25 = np.percentile(data, [75,25])    #Q3 is q75 which is 75 percentile and likewise Q1 is q25
  iqr = q75 - q25                            #interquartile range
  upper_range = q75 + 1.5*iqr
  lower_range = q25 - 1.5*iqr
  ans = list(filter(lambda x: x>upper_range or x<lower_range, data))
  return ans
# d = [10, 8, 9, 7, 6, 11, 7, 1, 9, 929, 100]
# print(outlier(d))

## Distribution Normality check
# Given an array consisting of various numbers, representing a distribution, check if the array follows a normal distribution. For the task, you aren't allowed to use any libraries, but rather try to solve the same using mean and standard deviation (hint: which method uses these parameters?).
# Take the margin of error for the test to be a 2% difference from the required values under standard deviations. What this means in simpler terms is, find what percent of data lies in one/two/three standard deviation.
# If the percentage observed is similar to the properties of the normal distribution with a margin of +- 2% then return "yes" the data is normal, else "no".
import math
def calculate_mean(arr):
  return sum(arr) / len(arr)
def calculate_standard_deviation(arr, mean):
  variance = sum((x - mean) ** 2 for x in arr) / len(arr)
  return math.sqrt(variance)
def check_normal_distribution(arr):
  mean = calculate_mean(arr)
  std_dev = calculate_standard_deviation(arr, mean)  
  within_1_std = sum(1 for x in arr if mean - std_dev <= x <= mean + std_dev) / len(arr) * 100
  within_2_std = sum(1 for x in arr if mean - 2 * std_dev <= x <= mean + 2 * std_dev) / len(arr) * 100
  within_3_std = sum(1 for x in arr if mean - 3 * std_dev <= x <= mean + 3 * std_dev) / len(arr) * 100
  print(f"Within 1 std: {within_1_std}%")  #theoretical values >> {#68.27% of the data should fall within 1 standard deviation.
  print(f"Within 2 std: {within_2_std}%")                          #95.45% of the data should fall within 2 standard deviations.
  print(f"Within 3 std: {within_3_std}%")                          #99.73% of the data should fall within 3 standard deviations.}  
  if (66.27 <= within_1_std <= 70.27) and (93.45 <= within_2_std <= 97.45) and (97.73 <= within_3_std <= 101.73):
    return "yes"
  else:
    return "no"
arr = [0.44122748688504143, -0.33087015189408764, 2.43077118700778, -0.2520921296030769, 0.10960984157818278, 1.5824811170615634, -0.9092324048562419, -0.5916366579302884, 0.18760322583703548, -0.32986995777935924]
# print(check_normal_distribution(arr))
