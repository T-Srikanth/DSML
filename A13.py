# Intermediate DSA: Contest 1
################################################
## Question 1 and 2 - didn't solve
## Removing Subarray     abs(arr[i]-arr[i+1]<=B)
# You are given an integer array A having length N. You have to tell the length of smallest subarray that can be removed from the array such that after removal, the values of each pair of adjacent elements
# left in the  array are atmost B apart i.e. after removal, abs(A[i]-A[i+1])<=B
# Note: An array with only single element is always a valid solution as it does not contain any adjacent elements.
def remove_sub(A, B):
  n =len(A)
  flag = True
  for i in range(n-1):
    if abs(A[i]-A[i+1])>B:
      flag=False
      break
  if flag == True:
    return 0
  lenl = 1
  for i in range(1,n):
    if abs(A[i]-A[i-1])<=B:
      lenl += 1
    else:
      break
  lenr =1
  for i in range(n-2,-1,-1):
    if abs(A[i]-A[i+1])<=B:
      lenr += 1
    else:
      break
  for l in range(1,n):
    i=0
    while i+l-1 < n:
      j = i+l-1
      if i-1<0:
        if(j+1>=n) or (n-(j+1)<=lenr):
          return l
      elif j+1>=n:
        if(i-1<0) or ((i-1)-1<=lenl):
          return l
      else:
        if((i-1)+1<=lenl) and (n-(j+1)<=lenr) and (abs(A[i-1]-A[j+1])<=B):
          return l
      i += 1
  return n
# A = [5,10,15,20]
# B = 4
# print(remove_sub(A, B))

## Matrix and Queries
# You are given a AxA 2D binary matrix in which elements are initially set to 0. You are also given a 2D matrix B(consisting of Q rows having 3 columns each).
# B[i] representing ith query. B consists of 3 types of queries:
# for B[i][0]=1,Print the sum of all elements of the matrix modulo 10^9+7.(B[i][1] and B[i][2] equals to 0 in this type)
# for B[i][0]=2,Invert the value in cell (B[i][1],B[i][2]), i.e.,Before processing this query, if the value at the cell was equal to X, then it becomes 1-X after the query
# for B[i][0]=3,Invert all the values in row B[i][1].(B[i][2] equals to 0 in this type)
def solve(A,B):
  mod = 1000000007
  Q = len(B)
  curr = 0
  cntInRow = [0]*A
  flipRow = [0]*A
  res = []
  for i in range(Q):
    t = B[i][0]
    r = B[i][1]
    c = B[i][2]
    if t == 1:
      res.append(curr)
    if t == 2:
      cnt=0
      for j in range(i+1):
        if B[j][0]==2 and B[j][1]==r and B[j][2]==c:
          cnt+=1
      r -= 1
      c -= 1
      cnt = (cnt+flipRow[r])%2
      if cnt%2 == 0:
        curr -= 1
        cntInRow[r] -= 1
      else:
        curr += 1
        cntInRow[r] += 1
    if t == 3:
      r -= 1
      flipRow[r] += 1
      curr -= cntInRow[r]
      cntInRow[r] = (A-cntInRow[r])
      curr += cntInRow[r]
    curr = (curr+mod)%mod
  return res
A = 3
B = [[1,0,0],
     [2,2,3],
     [3,1,0],
     [2,3,3],
     [1,0,0]]
print(solve(A,B))


## Generate Array
# You are given an array A of size N and you are required to generate another array B of size N. You have to find minimum value of B[i] for which summation of (A[i]&B[i]) for i=0 to i=N-1 is minimum possible.
# Also, you have to select B[i] such that (A[i]&B[i]) is a positive value. & is bitwise operator
# for input A=[1,2,3],output B=[1,2,1]; for input A=[2,8,9],output B=[2,8,1]
def gen_array(A):
  n = len(A)
  B = [0]*n
  for i in range(n):
    for j in range(7):
      if (A[i]&(1<<j))==(1<<j):
        B[i]=1<<j
        break
  return B
# A = [2,8,9]
# print(gen_array(A))

## Minimum Picks
# You are given an array of integers A of size N. Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.
def mini_picks(A):
  n = len(A)
  max_even = 0
  min_odd = 99999
  for i in range(n):
    if A[i]%2==0:
      max_even = max(max_even,A[i])
    else:
      min_odd = min(min_odd,A[i])
  res = max_even - min_odd
  return res
A = [5,17,100,1]
# print(mini_picks(A))

## Little Ponny and Maximum Element
# Little Ponny is given an array A of N integers. In a particular operation, he can set any element of the array equal to -1. He wants your help in finding out the minimum number of operations required 
# such that the maximum element of the resulting array is B. If it is not possible, then return -1.
def little_ponny(A,B):
  if B not in A:
    return -1
  count = 0
  for elem in A:
    if elem>B:
      count += 1
  return count
# A = [2,4,1]
# B = 3
# print(little_ponny(A,B))

## Alternating Subarrays
# You are given an integer array A of length N comprising of 0's and 1's, and an integer B. You have to tell all the indices of array A that can act as a centre of 2*B+1 length 0-1 alternating subarray.
# A 0-1 alternating array is an array containing only 0's and 1's, and having no adjacent 0's or 1's. For e.g. arrays [0,1,0,1],[1,0],[1] are 0-1 alternating, while [1,1] and [0,1,0,0,1] are not.
def alt_sub(A,B):
  n = len(A)
  sub_len = 2*B+1
  indices =[]
  for i in range(0, n-sub_len+1):
    state = A[i]
    for j in range(i,i+sub_len-1):
      if state!=A[j+1]:
        state = A[j+1]
      else:
        break
    indices.append(i+B)
  return indices
# A = [0,0,0,1,1,0,1]
# B=0
# print(alt_sub(A,B))