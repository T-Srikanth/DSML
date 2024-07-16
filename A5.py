# Arrays - Prefix Sum
###################################################
######### Reference links #########
#################################################### 

## Equilibrium index of an array
# You are given an array A of integers of size N. Your task is to find the equilibrium index of the given array
# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
# If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.
# Note: Array indexing starts from 0.
#       If there is no equilibrium index then return -1.
#       If there are more than one equilibrium indexes then return the minimum index.
# my solution
def equi_index(arr):
  n = len(arr)
  prefix_sum = [0]*n
  prefix_sum[0] = arr[0]
  for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
  equi_index_value = -1
  if(prefix_sum[n-1]-prefix_sum[0] == 0):  #if sum of elements from index 1 to n == 0 then 0 is the equilibrium index
    equi_index_value = 0
    return equi_index_value
  for i in range(1, n-1):
    if(prefix_sum[i-1] == prefix_sum[n-1] - prefix_sum[i]):  #if p[i-1] == p[n-1] - p[i]
      equi_index_value = i
      return equi_index_value
  if(prefix_sum[n-2] == 0): #if sum of elements from index 0 to n-2 == 0 then n-1 is the equilibrium index
    equi_index_value = n-1
    return equi_index_value
  return equi_index_value
# a = [2,-2,4,-4,7]
# equi_index(a)

#better solution
def solve(A):
  n = len(A)
  summ = 0
  for i in A:
    summ += i
  l = 0   # sum of elements at lower indexes
  for i in range(0, n):
    summ -= A[i]    # sum of elements at higher indexes
    if l == summ :
      return i
    l += A[i]
  # If no equilibrium index found, then return -1
  return -1

## Special Index
# Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
# example: A = [2, 1, 6, 4] should return 1; A = [1, 1, 1] should return 3
def special_index(arr):
  count = 0
  n = len(arr)
  for i in range(n):
    temp_arr = arr[:]
    del temp_arr[i]
    print(temp_arr)
    sum_even = 0
    sum_odd = 0
    for j in range(n-1):
      if j%2 == 0:
        sum_even += temp_arr[j]
      else:
        sum_odd += temp_arr[j]
    if sum_even == sum_odd :
        count += 1
    continue  
  return count         
# A = [1,2]
# print(special_index(A))

#better solution
def solve(A):
  n=len(A)
  if n==1:
    return 1
  if n==2:
    return 0
  sumEven = 0
  sumOdd = 0
  for i in range(n) : #calculate sum of elements at even indices and odd indices
    if (i % 2 == 0) :
      sumEven += A[i]

    else :
      sumOdd += A[i]
  currOdd = 0
  currEven = A[0]
  res = 0
  newEvenSum = 0
  newOddSum = 0
  for i in range(1,n-1): #to handle elements from first index to last but one index
    if i%2 :
      currOdd += A[i]
      newEvenSum = currEven + sumOdd- currOdd
      newOddSum = currOdd + sumEven - currEven - A[i]
    else :
      currEven += A[i]
      newOddSum = currOdd + sumEven  - currEven
      newEvenSum = currEven + sumOdd - currOdd -A[i]
    if (newEvenSum == newOddSum) :
      res+=1
  if (sumOdd == sumEven - A[0]) :  #to handle 0 index element
    res+=1
  if (n % 2 == 1) :  #to handle (n-1) last index element
    if (sumOdd == sumEven - A[n - 1]) :
      res+=1
  else :
    if (sumEven == sumOdd - A[n - 1]) :
      res+=1
  return res

## Pick from both sides!
# You are given an integer array A of size N. You have to perform B operations. 
# In one operation, you can remove either the leftmost or the rightmost element of the array A.
# Find and return the maximum possible sum of the B elements that were removed after the B operations.
# Note: Suppose B = 3, and array A contains 10 elements, then you can:
#           Remove 3 elements from front and 0 elements from the back, OR
#           Remove 2 elements from front and 1 element from the back, OR
#           Remove 1 element from front and 2 elements from the back, OR
#           Remove 0 elements from front and 3 elements from the back.
def pick_max(arr, ops):
  n = len(arr)
  pref = [0] * n
  pref[0] = arr[0]
  for i in range(1, n):
    pref[i] = pref[i-1] + arr[i]
  ans = pref[ops-1]
  suff_sum = 0
  for i in range(ops):
    suff_sum = suff_sum + arr[n-i-1]
    pref_sum = pref[ops-1-i] - arr[ops-1-i]
    ans = max(ans, pref_sum + suff_sum)
  return ans

# OR
def solve(A, B):
  sum , ans = 0, 0
  for i in range(B):
    sum += A[i]
    ans = sum
    r = len(A) - 1 
    l = B - 1
    while(l >= 0):
      sum -= A[l]
      sum += A[r]
      ans = max(ans,sum)
      l -= 1
      r -= 1
    return ans
# A = [5, -2, 3 , 1, 2]
# B = 3
# print(pick_max(A,B))

## Range Sum Query
# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
#my solution for single range
def range_sum(arr, start, end):
  n = len(arr)
  prefix_sum_arr = [0]*n
  prefix_sum_arr[0] = arr[0]
  for i in range(1, n):
    prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i]
  if(start == 0):
    res = prefix_sum_arr[end]
  else:
    res = prefix_sum_arr[end] - prefix_sum_arr[start-1]
  return res

# A = [2,2,2]
# print(range_sum(A, 0, 0))

#OR with B being an 2d array of multiple arrays
def rangeSum(A, B):
        n, m = len(A), len(B)
        pref = [0 for i in range(n + 1)]
        pref[0] = A[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + A[i]   
        ans = [0 for i in range(m)]
        for i in range(m):
            ans[i] = pref[B[i][1]] - (pref[B[i][0] - 1] if B[i][0] > 0 else 0)
        return ans

## Time to equality
# Given an integer array A of size N. In one second, you can increase the value of one element by 1.
# Find the minimum time in seconds to make all elements of the array equal.
def solve(A):
  n = len(A)
  val = 0
  for i in range(n):
    val = max(val, A[i])
  
  ans = 0
  for i in range(n):
    ans += val - A[i]
  return ans

## Product array puzzle
# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.
# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.
def solve(A):
  n = len(A)
  pref = [0] * n
  suff = [0] * n
  pref[0] = A[0]
  for i in range(1,n):
    pref[i] = pref[i - 1] * A[i]
  suff[n - 1] = A[n - 1]
  for i in range(n-2 , -1, -1):
    suff[i] = suff[i + 1] * A[i]
  ans = [0] * n
  for i in range(n):
    if(i == 0):
      ans[i] = suff[i + 1]
    elif i == n - 1:
      ans[i] = pref[i - 1]
    else:
      ans[i] = pref[i - 1] * suff[i + 1]
  return ans