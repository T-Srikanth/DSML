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
  # sorted_data = sorted(data)
  q75, q25 = np.percentile(data, [75,25])
  iqr = q75 - q25
  upper_range = q75 + 1.5*iqr
  lower_range = q25 - 1.5*iqr
  ans = list(filter(lambda x: x>upper_range or x<lower_range, data))
  return ans
d = [10, 8, 9, 7, 6, 11, 7, 1, 9, 929, 100]
print(outlier(d))
