# Arrays - Carry Forward
###################################################
######### Reference links #########
####################################################

## Special subsequences "AG"
# You have given a string A having Uppercase English letters. You have to find how many times subsequence "AG" is there in the given string.
# A = "ABCGAG" should return 3 and A = "GAB" should return 0
def special_sub(string):
  n = len(string)
  count_G = [0]*n
  print(count_G)
  count = 0
  ans = 0
  for i in range(n-1, -1, -1):
    if string[i]=="G":
      count += 1
    elif string[i]=="A":
      ans += count
  return ans
# A = "GAb"
# print(special_sub(A))

## Closest MinMax
# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.
# A = [1, 3, 2] should return 2 and A = [2, 6, 1, 6, 9] should return 3
def minMax(arr):
  ans, n = len(arr), len(arr)
  mini, maxi = min(arr), max(arr)
  min_index = -1
  for i in range(n-1, -1, -1):  #handles cases in which min is on the right boundary of the subarray
    if arr[i] == maxi and min_index != -1:
      ans = min(ans, min_index-i+1)
    if arr[i] == mini:
      min_index = i
  max_index = -1
  for i in range(n-1, -1, -1):  #handles cases in which max is on the right boundary of the subarray
    if arr[i] == mini and max_index != -1:
      ans = min(ans, max_index-i+1)
    if arr[i] == maxi:
      max_index = i
  return ans
# A = [2, 6, 1, 6, 9]
# print(minMax(A))

## Bulbs
# A wire connects N light bulbs. Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.
# Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.
# Note: 0 represents the bulb is off and 1 represents the bulb is on.
def bulbs(arr):
  state = 0
  ans = 0
  for i in range(0, len(arr)):
    if (arr[i] == state):
      ans += 1
      state = 1 - state
  return ans
# A = [1, 1, 0, 1]
# print(bulbs(A))

## Amazing Subarrays
# You are given a string S, and you have to find all the amazing substrings of S. An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
def amazing_sub(string):
  se = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
  n = len(string)
  count = 0
  for i in range(n):
    if string[i] in se:
      count += n-i
  return count

## Even Subarrays
# You are given an integer array A. Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.
# Return "YES" if it is possible; otherwise, return "NO" (without quotes).
def solve(A):
  if len(A)%2 == 0 and A[0]%2 == 0 and A[-1]%2 == 0: return "YES"
  return "NO"

## Leader in an array
# Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.
# Note: The rightmost element is always a leader.
def leader(arr):
  n = len(arr)
  curr_leader = arr[-1]
  ans = 1
  for i in range(n-2, -1, -1):
    if arr[i] > curr_leader:
      ans += 1
      curr_leader = arr[i]
  return ans
A = [16, 17, 4, 3, 5, 2]
print(leader(A))
