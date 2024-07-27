# Intermediate DSA: Hashing -2
###################################################
######### Reference links #########
# Python References:
# 1. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# 2. https://docs.python.org/3/tutorial/datastructures.html#sets
# 3. https://www.geeksforgeeks.org/python-dictionary/
# 4. https://www.geeksforgeeks.org/python-set-methods/
####################################################

## Subarray with given sum
# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B. If the answer does not exist return an array with a single integer "-1".
# First sub-array means the sub-array for which starting index in minimum.
def subarray_sum(A,B):
  n=len(A)
  ans = []
  for i in range(n):
    sum=0
    for j in range(i,n):
      sum += A[j]
      if sum>B:
        break
      elif sum == B:
        return A[i:j+1]
      else:
        continue
  return [-1]
# A = [5, 10, 20, 100, 105]
# B = 110
# print(subarray_sum(A,B))
#better solution
def solve(self, A, B):
  n = len(A)
  i = j = 0
  list = []
  sum = A[0]
  flag = False
  while j < n and i < n:
    if sum == B:
      # current window sum = B
      flag = True
      break
    elif sum < B:
      # current window sum < B
      if j + 1 == n:
        break
      j = j + 1
      sum = sum + A[j]
    else:
      # current window sum > B
      if i + 1 == n:
        break
      i = i + 1
      sum = sum - A[i - 1]
  if flag == False:
    return [-1]
  for k in range(i, j + 1):
    list.append(A[k])
  return list

## Diff k
# Given an array A of integers and another non negative integer B . Find if there exists 2 indices i and j such that A[i] - A[j] = B and i != j.
def diff(A,B):
  n=len(A)
  a_dict={}
  for i in range(n):
    if A[i]-B in a_dict or A[i]+B in a_dict:
      return 1
    else:
      if A[i] not in a_dict:
        a_dict[A[i]] = 1
  return 0
# A = [2,4,3]
# B = 2
# print(diff(A,B))

## Longest consecutive sequence
# Given an unsorted integer array A of size N. Find the length of the longest set of consecutive elements from array A.
def long_consec(A):
  n=len(A)
  ans=0
  for val in A:
    if val-1 in A:
      continue
    else:
      cnt=0                   
      while val in A:
        cnt+=1
        val+=1
      ans=max(ans,cnt)
  return ans
# A = [100, 4, 200, 1, 3, 2]
# print(long_consec(A))

## Distinct numbers in window
# You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.
# Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.
# Note: if B > N, return an empty array.
def distinct_num(A,B):
  n=len(A)
  ans=[]
  a_dict={}  #dict to store unique keys in the window of size B
  for i in range(B):   #this loop store keys and their count from 0th to (B-1)th element
    if A[i] in a_dict:
      a_dict[A[i]] += 1
    else:
      a_dict[A[i]] = 1
  ans.append(len(a_dict))    
  for j in range(B,n):   # j here points to the end index of the window of size B
    if A[j] in a_dict:   # first if-else statement adds the new element as the window slides
      a_dict[A[j]] += 1
    else:
      a_dict[A[j]] = 1
    element_to_remove = A[j-B]   #to remove the first element from the dict
    a_dict[element_to_remove] -= 1
    if a_dict[element_to_remove] == 0:
      del a_dict[element_to_remove]
    ans.append(len(a_dict))
  return ans
# A = [1, 1, 2, 2]
# B = 1
# print(distinct_num(A,B))
#OR
def dNums(self, A, B):
  n = len(A)
  ret = []
  m = {}
  for i in range(n):
    # Increase key
    if A[i] in m:
      m[A[i]] += 1
    else:
      m[A[i]] = 1
    if i - B + 1 >= 0:
      # Decrease key
      ret.append(len(m))
      m[A[i - B + 1]] -= 1
      # Remove if count becomes 0
      if m[A[i - B + 1]] == 0:
        del m[A[i - B + 1]]
  return ret

## Is Dictionary?
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted 
# lexicographically in this alien language else, return 0.
def is_dict(A,B):
  n=len(A)
  index=[0]*26
  for i in range(26):
    index[ord(B[i])-ord('a')]=i
  for i in range(n-1):
    word1 = A[i]
    word2 = A[i+1]
    flag = 0
    for k in range(min(len(word1),len(word2))):
      if word1[k] != word2[k]:
        if(index[ord(word1[k])-97] > index[ord(word2[k])-97]):
          return 0
        flag = 1
        break
    if flag == 0:
      if len(word1)>len(word2):
        return 0
  return 1
# A = ["fine", "none", "bush"]
# B = "qwertyuiopasdfghjklzxcvbnm"
# print(is_dict(A,B))

## Pairs with given XOR
# Given an integer array A containing N distinct integers. Find the number of unique pairs of integers in the array whose XOR is equal to B.
# Note: Pair (a, b) and (b, a) is considered to be the same and should be counted once.
def pair_xor(A,B):
  n=len(A)
  a_dict={}
  count=0
  for val in A:
    if val^B in a_dict:
      count += 1
    a_dict[val] = 1
  return count
A = [3, 6, 8, 10, 15, 50]
B = 5
print(pair_xor(A,B))
#OR
def xorPairCount(arr, x): 
  result = 0 # Initialize result 
  n=len(A)  
  # create empty set that stores the  
  # visiting element of array.  
  s = set() 
  for i in range(0, n):      
    # If there exist an element in set s 
    # with XOR equals to x^arr[i], that  
    # means there exist an element such  
    # that the XOR of element with arr[i]   
    # is equal to x, then increment count. 
    if(x ^ arr[i] in s): 
      result = result + 1          
    # Make element visited 
    s.add(arr[i]) 
    print(s)
  return result
# A = [3, 6, 8, 10, 15, 50]
# B = 5
# print(xorPairCount(arr=A,x=B))

## Valid Sudoku
# Determine if a Sudoku is valid, according to
def isValidSudoku(A):
  rows = [[False for i in xrange(9)] for j in xrange(9)]
  cols = [[False for i in xrange(9)] for j in xrange(9)]
  grids = [[False for i in xrange(9)] for j in xrange(9)]  
  for i in xrange(9):
    for j in xrange(9):
      if A[i][j] == '.':
        continue
      num = int(A[i][j])-1
      grid = (i/3)*3 + (j/3)
      if rows[i][num] or cols[j][num] or grids[grid][num]:
        return 0
      else:
        rows[i][num], cols[j][num], grids[grid][num] = True, True, True             
  return 1