# Intermediate DSA: Hashing -1
###################################################
######### Reference links #########
####################################################

## Common Elements
# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.
# Note: Each element in the result should appear as many times as it appears in both arrays.
#       The result can be in any order.
def common_elem(A,B):
  n=len(A)
  m=len(B)
  a_dict={}
  b_dict={}
  res = []
  for elem in A:
    if elem in a_dict:
      a_dict[elem] += 1
    else:
      a_dict[elem] = 1
  for elem in B:
    if elem in b_dict:
      b_dict[elem] += 1
    else:
      b_dict[elem] = 1
  for key in a_dict:
    if key in b_dict:
      for _ in range(min(a_dict[key],b_dict[key])):
        res.append(key)
  return res
# A = [2, 1, 4, 10]
# B = [3, 6, 2, 10, 10]
# print(common_elem(A,B))
#OR
def solve(A, B):
  n = len(A)
  m = len(B)
  hashmap = {}
  for i in range(n):
    if(hashmap.get(A[i]) == None):
      hashmap[A[i]] = 1
    else:
      hashmap[A[i]] += 1  
  ans =[] 
  for i in range(m):
    if(hashmap.get(B[i]) != None and hashmap[B[i]] != 0):
      ans.append(B[i])
      hashmap[B[i]] -= 1
  return ans

## First Repeating Element
# Given an integer array A of size N, find the first repeating element in it. We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
# If there is no repeating element, return -1.
def first_repeating(A):
  n=len(A)
  a_dict={}
  for elem in A:
    if elem in a_dict:
      a_dict[elem] += 1
    else:
      a_dict[elem] = 1
  for elem in A:
    if a_dict[elem] > 1:
      return elem
  return -1
# A = [6, 10, 5, 4, 9, 120]
# print(first_repeating(A))
#OR
def solve(self, A):
  n = len(A)
  # Initialize index of first repeating element
  mini = -1
  # Creates an empty hashset named ump
  ump = {}
  # Traverse the input array from right to left
  for i in range(n-1, -1, -1):
    # If element is already in hash set, update min
    if (ump.get(A[i]) != None):
      mini = i
    else:   # Else add element to hash set
      ump[A[i]] = 1
  if(mini == -1):
    return mini
  return A[mini]

## Subarray with 0 sum
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.
def sub_zero(A):  #idea is to find the prefix sum of the array and if the prefix sum value is zero or it repeats itself then there is a subarray satisfying the condition
  n=len(A)
  pref=[0]*n
  pref[0] = A[0]
  freq = {}
  for i in range(1,n):
    pref[i] = A[i] + pref[i-1]
  # print(pref)
  for val in pref:
    print(freq)
    if (val in freq) or val==0:
      return 1
    else:
      freq[val] = 1
  return 0
# A = [4, -1, 1]
# print(sub_zero(A))
# OR
def solve(A):
  d = {}
  curr_sum = 0
  for x in A:
    curr_sum += x
    if curr_sum == 0 or x == 0 or curr_sum in d:
      return 1
    else:
      d[curr_sum] = 1
  return 0  

## Shaggy and distances
# Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.
# Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.
def shaggy(A):
  n=len(A)
  a_dict = {}  #a_dict[i] holds the previous index value where the same element occurred
  min_distance = n
  for i in range(n):
    if A[i] in a_dict:
      min_distance = min(min_distance, i-a_dict[A[i]])
      a_dict[A[i]] = i  #if there are more than 2 occurrences of same element
    else:
      a_dict[A[i]] = i
  if min_distance == n:
    return -1
  return min_distance
# A = [1, 2,4,1,3,1]
# print(shaggy(A))

## Largest Continuous Sequence Zero Sum
# Given an array A of N integers. Find the largest continuous sequence in a array which sums to zero.
def large_zero(A):
  n=len(A)
  pref = [0]*n
  pref[0] = A[0]
  a_dict = {0: -1}  #initialising with 0: -1 because if the sum of the total array is 0 then n should be returned
  start,end=0,0     #a_dict will store index value when the particular sum first occurred 
  for i in range(1,n):
    pref[i] = A[i] + pref[i-1]
  for i in range(n):
    if pref[i] in a_dict:
      if i-a_dict[pref[i]] > end-start:
        start = a_dict[pref[i]]
        end = i
    else:
      a_dict[pref[i]] = i
  res = A[start+1:end+1]
  return res
# A = [1,2,-2,4,-4,6,-6,3,-4]
# print(large_zero(A))
#OR
def lszero(self, A):
  mp = {0:-1}
  s = 0
  start = end = 0
  for i in range(len(A)) :
    s += A[i]
    if s in mp :
      if i - mp[s] > end - start :
        start = mp[s]
        end = i 
    else :
      mp[s] = i
  return A[start+1:end+1]

## K Occurrences
# Groot has N trees lined up in front of him where the height of the i'th tree is denoted by H[i]. He wants to select some trees to replace his broken branches.
# But he wants uniformity in his selection of trees. So he picks only those trees whose heights have frequency B. He then sums up the heights that occur B times. 
# (He adds the height only once to the sum and not B times). But the sum he ended up getting was huge so he prints it modulo 10^9+7. In case no such cluster exists, Groot becomes sad and prints -1.
def k_occur(A,B):
  mod = 1000000007
  n=len(A)
  a_dict = {}
  res = 0
  for i in range(n):
    if A[i] in a_dict:
      a_dict[A[i]] += 1
    else:
      a_dict[A[i]] = 1
  for k,v in a_dict.items():
    if v == B:
      res += k
      res %= mod
  return -1 if res==0 else res
# B=2
# C=[1, 2, 2, 3, 3]
# print(k_occur(C,B))
## Check Palindrome - 2
# Given a string A consisting of lowercase characters. Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.
def check_pal(A):
  n=len(A)
  a_dict={}
  for i in range(n):
    if A[i] in a_dict:     #in case of even length string there can be maximum one odd occurance of a character, but since only one odd occurance can't occur independently in an even length string
      a_dict[A[i]] += 1    #we can just check if the odd occurances > 1 condition for both even length and odd length string input
    else:
      a_dict[A[i]] = 1
  flag = 1
  odd_occurances = 0
  for key in a_dict:
    if a_dict[key]%2 != 0:
      odd_occurances += 1
  if odd_occurances>1:
    flag = 0
  return flag
# A = "abbaee"
# print(check_pal(A))

## Colorful Number
# Given a number A, find if it is COLORFUL number or not. If number A is a COLORFUL number return 1 else, return 0. What is a COLORFUL Number:
# A number can be broken into different consecutive sequence of digits.  The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
# This number is a COLORFUL number, since the product of every consecutive sequence of digits is different
def colorful_num(A):
  string=str(A)
  s_list=list(string)
  int_list=[int(i) for i in s_list]
  n=len(int_list)
  i_dict={}
  for i in range(n):
    prod=1
    for j in range(i,n):
      prod*=int_list[j]
      if prod in i_dict:
        return 0
      else:
        i_dict[prod] = 1
  return 1
# A = 3245
# print(colorful_num(A))
#OR
def findProd(A):
  ret = 1
  for a in A:
    ret *= int(a)
  return str(ret)

def colorful(A):
  numbers = dict()
  strA = str(A)
  for a in strA:
    if a in numbers:
      return 0
    else:
      numbers[a] = 1
  n = len(strA)
  for i in range(2, n + 1):
    for j in range(n - i + 1):
      num = strA[j : j + i]
      ret = findProd(num)
      if ret in numbers:
        return 0
      else:
        numbers[ret] = 1
  return 1