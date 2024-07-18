# Arrays - Subarrays
###################################################
######### Reference links #########
####################################################

## Sum of all subarrays
# You are given an integer array A of length N. You have to find the sum of all subarray sums of A.
# More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array. A subarray sum denotes the sum of all the elements of that subarray.
# Note : Be careful of integer overflow issues while calculations. Use appropriate datatypes.
def sum_subarray_sums(arr):     # arr = [a0, a1, a2] 
  n = len(arr)            #sub_arrays:  [a0]          [a1]      [a2] 
  sum = 0                              #[a0, a1]      [a1, a2]
  for i in range(n):                   #[a0, a1, a2]
    sum += (n-i)*(i+1)*arr[i]    #count number of times each element occurs
  return sum                     
# A = [2, 1, 3]
# print(sum_subarray_sums(A))

## Max sum contiguous subarray
# Find the maximum sum of contiguous non-empty subarray within an array A of length N.
# my solution
def max_subarray_sum(arr):
  n = len(arr)
  max_sum = arr[0]
  for i in range(n):
    tmp_sum = 0
    for j in range(i,n):
      tmp_sum += arr[j]
      max_sum = max(max_sum, tmp_sum)
  return max_sum
# A = [3, 7, 90, 20, 10, 50, 40]
# print(max_subarray_sum(A))

#better solution
def maxSubArray(A):
  max_ending_here = max_so_far = A[0]
  for x in A[1:]:
    max_ending_here = max(x, max_ending_here+x)
    max_so_far = max(max_so_far, max_ending_here)
  return max_so_far

## Subarray with least average
# Given an array A of size N, find the subarray of size B with the least average.
def least_average(arr, B):  #comparing least subarray totals instead of average as average is total/fixed_value
  n = len(arr)
  pref_sum = []
  pref_sum.append(arr[0])
  for i in range(1, n):
    pref_sum.append(pref_sum[i-1]+arr[i])
  res = pref_sum[B-1]
  ind = 0
  for i in range(1, n-B):
    if (res > pref_sum[i+B-1] - pref_sum[i-1]):
      res = pref_sum[i+B-1] - pref_sum[i-1]
      ind = i
  return ind
# A = [3, 7, 5, 20, -10, 0, 12]  
# least_average(A,2)

# better solution as space complexity is O(1) instead of O(n) from my solution
def solve(A, B):
  res=0
  summ=0
  for i in range(B) :
    summ+=A[i]
  n=len(A)
  min_sum=summ
  for i in range(B,n) :
    summ+=A[i]-A[i-B]
    if(summ<min_sum) :
      min_sum=summ
      res=i-B+1
    return res


## Maximum subarray easy
# You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum. But the sum must not exceed B.
def max_subarray_sum(A, B, C):
  ans = 0
  for i in range(A):
    sum = 0
    for j in range(i, A):
      sum += C[j]
      if (sum <= B):
        ans = max(ans, sum)
      else:
        break
  return ans

## Counting subarrays
# Given an array A of N non-negative numbers and you are also given non-negative number B.
# You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow.
def max_subarray_count(A, B):
  count = 0
  n = len(A)
  for i in range(n):
    sum = 0
    for j in range(i, n):
      sum += A[j]
      if (sum <= B):
        count += 1
      else:
        break
  return count
# A = [1, 11, 2, 3, 15]
# B = 10
# print(max_subarray_count(A,B))

## Good subarrays easy
# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.
def good_subarray(arr, B):
  count = 0
  n = len(arr)
  for i in range(n):
    sum = 0
    for j in range(i, n):
      sum += arr[j]
      if (j-i+1)%2==0 and sum<B:
        count += 1
      elif (j-i+1)%2!=0 and sum>B:
        count += 1
  return count
# A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
# B = 65
# print(good_subarray(A,B))

## Alternating subarrays easy
# You are given an integer array A of length N comprising of 0's & 1's, and an integer B. You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.
# A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.
def alt_subarray(arr, B):
  n = len(arr)
  sub_length = 2*B+1
  res = []
  for i in range(n-sub_length+1):
    curr_val = arr[i]
    flag = 1
    for j in range(i+1, i+sub_length):
      if arr[j] == curr_val:
        flag = 0
        break
      curr_val = arr[j]
    if(flag == 1):
      res.append(i+B)
  return res

# A = [0, 0, 0, 1, 1, 0, 1]
# B = 0 
# print(alt_subarray(A,B))

    
