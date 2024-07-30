# Intermediate DSA: Sunsequences & Subsets
###################################################
######### Reference links #########
####################################################

## Sum the difference
# Given an integer array, A of size N. You have to find all possible non-empty subsequences of the array of numbers and then, for each subsequence, 
# find the difference between the largest and smallest number in that subsequence. Then add up all the differences to get the number. As the number may be large, output the number modulo 1e9 + 7 (1000000007).
# Note: Subsequence can be non-contiguous.
def sum_of_diff(A):
  # sum(max-min) == sum(max) - sum(min)
  n=len(A)
  max_sum=0
  mod=1000000007
  A.sort()
  for i in range(n):
    max_sum += A[i]*(2**i)%mod #max number of an array contributes to the sum (2 power (len(A)-1)) times and next highest (2 power (len(A)-2)) times and so on..
  min_sum=0
  for i in range(n):
    min_sum += A[i]*(2**(n-1-i))%mod #min number of an array contributes to the sum (2 power (len(A)-1)) times and next minimum (2 power (len(A)-2)) times and so on..
  return max_sum-min_sum
# A = [3, 5, 10] 
# print(sum_of_diff(A))

## Find subsequence
# Given two strings A and B, find if A is a subsequence of B. Return "YES" if A is a subsequence of B, else return "NO".
def find_sub(A,B):
  n=len(A)
  m=len(B)
  j=0
  for i in range(n):
    if A[i] in B:
      j=B.index(A[i])
      B=B[j:]
    else:
      return "NO"
  return "YES"
# A = 'mcbzcsqvouyrsq'
# B = 'wnqryjentzuptshyjvufcbhkcorfchzvhotqwctvgjjhmfcrsminuvabryqplqarmbsxewaumd'    
# print(find_sub(A,B))
#OR
def solve(A, B):
  n = len(A)
  m = len(B)
  i = 0
  j = 0
  while(i < n and j < m):
    if(A[i] == B[j]):
      i += 1
      j += 1
    else:
      j += 1
  if i == n:
    return "YES"
  return "NO"

## Subsequence-Sum Problem
# You are given an array of integers A of N size. You have to find that there is any subsequence exists or not whose sum is equal to B.
# Note: A subsequence is a sequence that can be derived from the given array by deleting zero or more elements without changing the order of the remaining elements.
def sub_sum(A,B):
  n=len(A)
  for i in range(2**n):
    sum=0
    for j in range(n):
      if i & (1<<j) != 0:
        sum += A[j]
    if sum == B:
      return True
  return False
# A = [2, 2, 2, 2]
# B = 5
# print(sub_sum(A,B))
#OR
def solve(self, A, B):
  if B == 0:
    return 0
  n = len(A)
  def subsequenceSum(A, B, i):
    if i == -1:
      if B == 0:
        return 1
      return 0
    ans = 0
    ans |= subsequenceSum(A, B, i-1)
    ans |= subsequenceSum(A, B - A[i], i-1)
    return ans
  return subsequenceSum(A, B, n-1)

## Odd Even Subsequences
# Given an array of integers A of size, N. Find the longest subsequence of A, which is odd-even. A subsequence is said to be odd-even in the following cases:
#     The first element of the subsequence is odd; the second element is even, the third element is odd, and so on. For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]
#     The first element of the subsequence is even, the second element is odd, the third element is even, and so on. For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]
# Return the maximum possible length of odd-even subsequence.
# Note: An array B is a subsequence of an array A if B can be obtained from A by deleting several (possibly, zero, or all) elements.
def odd_even(A):
  n=len(A)
  ans=0
  odd_start=1
  len_odd=0
  len_even=0
  for i in range(n):
    if A[i]%2==odd_start:
      len_odd += 1
      odd_start = 1-odd_start
    ans=max(ans,len_odd)
  even_start=0
  for i in range(n):
    if A[i]%2==even_start:
      len_even += 1
      even_start = 1-even_start
    ans=max(ans,len_even)
  return ans
# A = [2, 2, 2, 2, 2, 2]
# print(odd_even(A))
#OR
def solve(A):
  n=len(A)
  ans1, ans2 = 0, 0
  x, y = 1, 0 
  for it in A:
    it=(it&1)
    if(it==x):
      ans1+=1
      x^=1        
    if(it==y):
      y^=1
      ans2+=1  
  return max(ans1,ans2)


## Subarray OR
# You are given an array of integers A of size N. The value of a subarray is defined as BITWISE OR of all elements in it. Return the sum of value of all subarrays of A % 109 + 7.
MOD = 10**9 + 7
def sum_of_subarray_ORs(A):
  N = len(A)
  max_bit = 32  # Since we are dealing with integers, 32 bits is enough
  total_sum = 0  
  # Track the last seen index of each bit being set
  last_seen = [-1] * max_bit  
  # Iterate over each element in the array
  for i in range(N):
    # Update the last seen index for each bit
    for bit in range(max_bit):
      if (A[i] & (1 << bit)) != 0:
        last_seen[bit] = i    
    # Add contributions of each bit to the total sum
    for bit in range(max_bit):
      if last_seen[bit] != -1:
        # Number of subarrays ending at i with bit `bit` set
        num_subarrays_with_bit_set = last_seen[bit] + 1
        total_sum = (total_sum + (num_subarrays_with_bit_set * (1 << bit)) % MOD) % MOD  
  return total_sum
# A = [1, 2, 3]
# print(sum_of_subarray_ORs(A))

## Subset
# Given a set of distinct integers A, return all possible subsets.
# Note:   Elements in a subset must be in non-descending order.
#         The solution set must not contain duplicate subsets.
#         Also, the subsets should be sorted in ascending ( lexicographic ) order.
#         The initial list is not necessarily sorted.
class Solution:
  # @param A : list of integers
  # @return a list of list of integers
  def subsets(self, A):
    A.sort()
    return get_subsets(A)
def get_subsets(A):
  if not A:
    return [[]]
  new = get_subsets(A[1:])
  old = [[A[0]] + x for x in new]
  ans  = [[]] + old + new[1:]
  return ans
#####
class Solution:
  def subsets(self, A):
    A.sort()  # Sort the input list to ensure non-descending order of elements in subsets
    result = []
    self.backtrack(A, 0, [], result)
    return result
  def backtrack(self, A, index, path, result):
    result.append(path)  # Append the current subset to the result
    for i in range(index, len(A)):
      self.backtrack(A, i + 1, path + [A[i]], result)
# solution = Solution()
# A = [3, 1, 2]
# print(solution.subsets(A))

## Little Ponny and 2-Subsequence
# Little Ponny has been given a string A, and he wants to find out the lexicographically minimum subsequence from it of size >= 2. Can you help him?
# A string a is lexicographically smaller than string b, if the first different letter in a and b is smaller in a. For example,
# "abc" is lexicographically smaller than "acc" because the first different letter is 'b' and 'c' which is smaller in "abc".
def little(A):
  n=len(A)
  mini=A[0]
  for i in range(1,n-1):
    if A[i]<mini:
      mini=A[i]
  ind=A.index(mini)
  A=A[ind+1:]
  new_mini=A[0]
  for i in range(1,len(A)):
    if A[i]<new_mini:
      new_mini=A[i]
  return mini+new_mini
# A = "ksdjgha" 
# little(A)
#OR
class Solution:
  # @param A : string
  # @return a strings
  def solve(self, A):
    minchar = 'z'
    idx = 1000000000
    for i in range(len(A) - 1):
      if A[i] < minchar:
        minchar = A[i]
        idx = i
    
    minchar2 = 'z'
    for i in range(idx + 1, len(A)):
      if(A[i] < minchar2):
        minchar2 = A[i]
    
    ans = minchar + minchar2
    return ans