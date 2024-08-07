# Intermediate DSA: Stacks and Queues - Basics
###################################################
######### Reference links #########
# https://www.scaler.com/topics/data-structures/stacks-in-data-structure/
# Queue Implementation Details: https://www.interviewbit.com/tutorial/queue-implementation-details/#queue-implementation-details
####################################################

## Perfect Numbers
# Given an integer A, you have to find the Ath Perfect Number. A Perfect Number has the following properties:
#     It comprises only 1 and 2.
#     The number of digits in a Perfect number is even.
#     It is a palindrome number.
# For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.
from collections import deque
def num_list(A):
  digits = [1,2]
  qu = deque(digits)
  ans = -1
  while A>0:
    ans = qu.popleft()
    for digit in digits:
      new_val = ans*10 + digit
      qu.append(new_val)
    if is_perfect(ans):
      A -= 1
  return ans
def is_perfect(B):
  str_B = str(B)
  if len(str_B)%2==0 and is_palindrome(str_B):
    return True
  return False  
def is_palindrome(string):
  i,j=0,len(string)-1
  while i<j:
    if string[i]!=string[j]:
      return False
    i += 1
    j -= 1
  return True    
# print(num_list(2))

## N integers containing only 1,2 & 3
# Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.
# Note: All the A integers will fit in 32-bit integers.
def n_int(digits,A):
  qu = deque(digits)
  ans = []
  for i in range(A):
    tmp = qu.popleft()
    for digit in digits:
      qu.append(tmp*10 + digit)
    ans.append(tmp)
  return ans
# print(n_int([1,2,3],7))

## Reversing Elements of Queue
# Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, leaving the other elements in the same relative order. 
# Note: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.
def partial_reverse(A,B): #assuming B is always less than len(A)
  i,j=0,B-1
  while i<j:
    A[i],A[j]=A[j],A[i]
    i += 1
    j -= 1
  return A
# A = [5, 17, 100, 11]
# B = 2
# print(partial_reverse(A,B))
#using queues
from collections import deque
class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return a list of integers
  def solve(self, A, B):
    n = len(A)
    if n < 2:
      return A
    q = deque()
    # Insert first B elements in queue
    for i in range(B):
      q.append(A[i])
    i = B - 1
    # Reverse the first B elements in the array A
    while len(q) != 0:
      A[i] = q.popleft()
      i -= 1
    return A
  
## Passing game
# There is a football event going on in your city. In this event, you are given A passes and players having ids between 1 and 106. Initially, some player with a given id had the ball in his possession. 
# You have to make a program to display the id of the player who possessed the ball after exactly A passes. There are two kinds of passes:
# 1) ID
# 2) 0
# For the first kind of pass, the player in possession of the ball passes the ball "forward" to the player with id = ID. For the second kind of pass, the player in possession of the ball 
# passes the ball back to the player who had forwarded the ball to him. In the second kind of pass "0" just means Back Pass. Return the ID of the player who currently possesses the ball.
def passing_game(A,B,C):  #A is num of passes, B is intial player ID, C is list of IDs(0 means back pass) 
  qu = deque([B])
  for i in range(A):
    if C[i] != 0:
      qu.append(C[i])
    else:
      qu.pop()            #LIFO approach which resembles a stack
  return qu.pop()
# A = 1
# B = 1
# C = [2]
# print(passing_game(A,B,C))
#OR
class Solution:
  def solve(self, A, B, C):
    stack = [B]
    for i in C:
      # pop from stack
      if i == 0:
        stack.pop()
      # push the given ID to stack
      else:
        stack.append(i)
    return stack[-1]

## Balanced Parantheses
# Given a string A consisting only of '(' and ')'. You need to find whether parentheses in A are balanced or not, if it is balanced then return 1 else return 0.
def balanced_para(string):  #stack approach here
  stack = []
  for char in string:
    if char == '(':
      stack.append(char)
    else:
      if len(stack)>0:
        stack.pop()
      else:
        return 0
  return 1 if len(stack)==0 else 0
# A = "(()"
# print(balanced_para(A))

## Task Scheduling
# A CPU has N tasks to be performed. It is to be noted that the tasks have to be completed in a specific order to avoid deadlock. In every clock cycle, the CPU can either perform a task or move it to the 
# back of the queue. You are given the current state of the scheduler queue in array A and the required order of the tasks in array B.
# Determine the minimum number of clock cycles to complete all the tasks.
def task_scheduling(A,B):
  cycles = 0
  qu = deque(A)
  for task in B:
    process = qu.popleft()
    while process != task: #to count cycles when the process is moved to back of the queue
      cycles += 1
      qu.append(process)
      process = qu.popleft()
    cycles += 1  #to count the cycle when the task is performed
  return cycles
A = [1]
B = [1]
print(task_scheduling(A,B))