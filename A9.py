# Arrays - Interview Questions
###################################################
######### Reference links #########
####################################################

## Length of longest consecutive ones
# Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.
def longest_ones(string):
  ans = 0
  n = len(string)
  left_ones = [0]*n  #list to store number of consecutive ones on the left of ith index till ith index 
  right_ones = [0]*n  #list to store number of consecutive ones on the right of ith index till ith index 
  total_ones = 0  #total number of ones in the string
  for i in range(n):
    if string[i] == '1':
      total_ones += 1
  left_ones[0] = int(string[0])    
  for i in range(1, n):  #loop to generate left_ones array
    if string[i] == '1':
      left_ones[i] = left_ones[i-1]+1
    else:
      left_ones[i] = 0
  right_ones[n-1] = int(string[n-1])
  for i in range(n-2, -1, -1):  #loop to generate right_ones array
    if string[i] == '1':
      right_ones[i] = right_ones[i+1]+1
    else:
      right_ones[i] = 0

  if len(string) == total_ones:  #to handle all 1s in a string
    return total_ones    
  for i in range(n):
    if string[i] == '0':
      if i == 0:  #to handle first character
        if right_ones[i+1]+1 < total_ones:
          ans = max(ans, right_ones[i+1]+1)
        else:
          ans = max(ans, right_ones[i+1])
      elif i == n-1:  #to handle last character
        if left_ones[i-1]+1 < total_ones:
          ans = max(ans, left_ones[i-1]+1)
        else:
          ans = max(ans, left_ones[i-1])
      else:
        if left_ones[i-1]+right_ones[i+1]+1 < total_ones:
          ans = max(ans, left_ones[i-1]+right_ones[i+1]+1)
        else:
          ans = max(ans, left_ones[i-1]+right_ones[i+1])
  return ans
# A = "111000"
# print(longest_ones(A))
# OR
def solve(A):
  # To count all 1's in the string
  cnt_one = 0
  n = len(A)
  for x in A:
    if x=='1':
      cnt_one+=1
  # To store cumulative 1's
  left = [0]*n
  right = [0]*n
  if A[0]=='1':
    left[0] = 1
  if A[n-1]=='1':
    right[n-1] = 1
  for i in range(1, n):
    if A[i]=='1':
      left[i] = left[i-1] + 1
  for i in range(n-2, -1, -1):
    if A[i]=='1':
      right[i] = right[i + 1] + 1
  cnt = 0
  max_cnt = 0
  for i in range(n):
    max_cnt = max(max_cnt, max(right[i], left[i]))
  for i in range(1, n-1):
    if A[i]=='0':
      su = left[i-1] + right[i+1]
      cnt = su
      if su < cnt_one:
        cnt += 1
      max_cnt = max(max_cnt, cnt)
      cnt = 0
  return max_cnt

## Chritmas Trees
# You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), 
# and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r. The cost of these trees is Bp + Bq + Br. 
# You are to choose 3 trees such that their total cost is minimum. Return that cost. If it is not possible to choose 3 such trees return -1.
def chritmas(A,B):
  n=len(B)
  if n < 3:
    return -1
  minimum = float('inf')
  for j in range(1,n-1):
    left_min = float('inf')
    right_min = float('inf')
    for i in range(j):
      if A[i]<A[j] and B[i]<left_min:
        left_min = B[i]
    for k in range(j+1,n):
      if A[k]>A[j] and B[k]<right_min:
        right_min = B[k]
    minimum = min(minimum, left_min + B[j] + right_min)
  return -1 if minimum == float('inf') else minimum
# A = [1, 6]
# B = [2, 5]
# print(chritmas(A,B))


## Spiral Order Matrix - 1
# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.
def spiral_matrix_gen(A):
  size = A
  i,j = 0,0
  val = 1
  ans = [[0]*A for i in range(A)]
  while i < size//2:
    for k in range(1,A):
      ans[i][j] = val
      val += 1
      j += 1
    for k in range(1,A):
      ans[i][j] = val
      val += 1
      i += 1
    for k in range(1,A):
      ans[i][j] = val
      val += 1
      j -= 1
    for k in range(1,A):
      ans[i][j] = val
      val += 1
      i -= 1
    i += 1
    j += 1
    A -= 2
  if size%2 != 0:
    center = size//2
    ans[center][center] = size*size
  return ans
# print(spiral_matrix_gen(5))


## Spiral Order Matrix - 2
# Given an integer A, Print an A X A square matrix filled with elements from 1 to A2 in spiral order.
# Note: Integers in same line are to be separated by single spaces.
def mat_printer(A):
  i, j = 0, 0
  val = 1
  mat = [[0]*A for i in range(A)]
  while i<A:
    if i%2 == 0:
      for j in range(A):
        mat[i][j] = val
        val += 1
    else:
      for j in range(A-1, -1, -1):
        mat[i][j] = val
        val += 1
    i += 1 
  for i in range(A):
    for j in range(A):
      print(mat[i][j], end=" ")
      val += 1
    print()
# mat_printer(2)

#OR
def printer():
  A = int(input())
  for i in range(1, A + 1):
    lo = (i - 1) * A + 1
    hi = (i - 1) * A + A
    p = 1
    if i % 2 == 0:
      temp = lo
      lo = hi
      hi = temp
      p = -1    
    j = lo
    while True:
      print (j, end = ' ')
      if j == hi:
          break
      j += p  
    print()  
  return 0

## Maximum positivity
# Given an array of integers A, of size N. Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.
# Note: It is guaranteed that an answer always exists.
def max_pos(arr):
  n = len(arr)
  ans = []
  count = 0
  final_count = 0
  for i in range(n):
    if arr[i] >= 0:
      count += 1
    if count > final_count:
      start_index = i-count+1
    final_count = max(final_count, count)
    if arr[i] < 0:
      count = 0
  for j in range(start_index, start_index+final_count):
    ans.append(arr[j])
  return ans
# A = [-1, 6, 8,-1,10,1,2,3,4,5,6,7,800,-1,-1, 10,7, 8,9,10,1,1,2,-1,2,5,6]
# print(max_pos(A))

#OR
def solve(A):
  ret = [[]]
  for i in A:
    if i < 0:
      ret.append([])
    else:
      ret[-1].append(i)
  mxlen = max([len(i) for i in ret])
  for i in ret:
    if len(i) == mxlen:
      return i

## Star Pattern - 1
# Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.
# ********    for input N=4
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********
def diamond(A):
  i=0
  while i<A:
    for j in range(A-i):
      print('*', end='')
    for j in range(2*i):
      print(' ', end='')
    for j in range(A-i):
      print('*', end='')
    print()
    i += 1
  i -= 1
  while i>=0:
    for j in range(A-i):
      print('*', end='')
    for j in range(2*i):
      print(' ', end='')
    for j in range(A-i):
      print('*', end='')
    print()
    i -= 1
# diamond(4)

#OR
def main():
  n = int(input())
  for i in range (n,0,-1):
    print("*"*i + " "*(2*(n-i))+"*"*i)
  for i in range (1,n+1):
    print("*"*i + " "*(2*(n-i))+"*"*i)


## Star Pattern - 2
# Write a program to input an integer N from user and print hollow inverted right triangle star pattern of N lines using '*'.
# *******    for input N=7
# *    *
# *   *
# *  *
# * *
# **
# *
def right_triangle(A):
  print('*'*A)
  for i in range(A-3, -1, -1):
    print('*' + ' '*i + '*')
  print('*')
# right_triangle(3)

#OR
def main():
  n = int(input())
  for i in range(1,n+1):
    for j in range(i,n+1):
      if i==j or i==1 or j==n:
        print('*',end='')
      else:
        print(' ',end='')
    print()
  return 0