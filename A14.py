# Intermediate DSA: Sorting
###################################################
######### Reference links #########
# Implementation Details:
# https://www.interviewbit.com/tutorial/sort-implementation-details/
# Tim Sort : 
# https://www.youtube.com/watch?v=_dlzWEJoU7I
# Comparators in Python:
# https://portingguide.readthedocs.io/en/latest/comparisons.html
# https://blog.devgenius.io/python-customize-sorting-in-several-ways-3961b648d31f
# https://www.pythonpool.com/python-__lt__/
####################################################

## Noble Integer
# Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.
def noble_int(A):
  n = len(A)
  A.sort(reverse=True)
  count = 0 if A[0]!=0 else 1
  # print(A)
  for i in range(1,n):
    curr_greater_count = 0
    if A[i]!=A[i-1]:
      curr_greater_count += i
      if curr_greater_count == A[i]:
        count +=1
  return 1 if count > 0 else -1
# A=[1, 1, 3, 3]
# print(noble_int(A))

#OR
def solve(A):
  inputSize = len(A)
  A.sort()
  start = A[0]
  for i in range(inputSize):
    if (start != A[i]) and (start == (inputSize - i)):
      return 1
    start = A[i]
  if start == 0:
    return 1
  return -1

## Elements Removal
# Given an integer array A of size N. You can remove any element from the array in one operation. The cost of this operation is the sum of all elements in the array present before this operation.
# Find the minimum cost to remove all elements from the array.
def elem_removal(A):
  n = len(A)
  A.sort(reverse=True)
  cost = 0
  for i in range(n):
    cost += (i+1)*A[i]
  return cost
# A = [2, 1,3]
# print(elem_removal(A))

## Largest Number
# Given an array A of non-negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.
from functools import cmp_to_key
def largest_num(A):
  def compare(x,y):
    if x+y < y+x:
      return 1
    elif x==y:
      return 0
    else:
      return -1
  nums = [str(num) for num in A]
  nums.sort(key=cmp_to_key(compare))
  if nums[0] == '0':
    return '0'
  return ''.join(nums)
# A = [0, 0,0,0,0]
# print(largest_num(A))

## Arithmetic Progression
# Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
def is_ap(A):
  n = len(A)
  A.sort()
  for i in range(1,n-1):
    if A[i]-A[i-1]!=A[i+1]-A[i]:
      return 0
  return 1
# A = [3, 5, 1,7,9]
# print(is_ap(A))

## Sort by Color
# Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will represent the colors as,
# red -> 0
# white -> 1
# blue -> 2
# Note: Using the library sort function is not allowed.
def sort_by_color(A):
  n = len(A)
  for i in range(n):
    for j in range(i,n):
      if A[i]>A[j]:
        A[i],A[j]=A[j],A[i]
  return A
A = [0, 1, 2, 0, 1, 2]
print(sort_by_color(A))

#better solution
def sortColors(A):
  n = len(A)
  i = 0
  j = n - 1
  k = n - 1
  while i < k:  #this loop runs until i becomes k, k and j are poiters starting from end of the array
    if A[i] == 0:
      i += 1
    elif A[i] == 1:
      if i < j:
        A[i],A[j] = A[j],A[i]
        j-=1
      else:
        i+= 1
    else:
      A[i],A[k] = A[k],A[i]
      k -= 1
      if j > k:
        j = k
  return A