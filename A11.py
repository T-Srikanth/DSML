# Bit Manipulations - 2
###################################################
######### Reference links #########
####################################################

## Help from Sam
# Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a target score of A for himself. Initially, Alex's score was zero. Alex can double his score by doing a question, 
# or Alex can seek help from Sam for doing questions that will contribute 1 to Alex's score. Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.
# Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A.
def help_from_sam(A):  #it's basically asking for number of set bits in A
  help_number = 0
  while A!=0:
    A = A&(A-1)
    help_number += 1
  return help_number
# print(help_from_sam(5))

#OR
def solve(A):
  ans=0
  while(A):
    if(A&1 == 1):
      ans += 1
    A >>= 1
  return ans

## Finding Good Days
# Alex has a cat named Boomer. He decides to put his cat to the test for eternity. He starts on day 1 with one stash of food unit, every next day, the stash doubles.
# If Boomer is well behaved during a particular day, only then she receives food worth equal to the stash produced on that day. Boomer receives a net worth of A units of food. What is the number of days she received the stash?
def good_days(A): #this is also number of set bits in A
  days = 0
  while A!=0: 
    A = A&(A-1)  #this line unsets the righmost bit of A and assigns that value back to A
    days += 1
  return days
# print(good_days(8))

## Single Number
# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice. Find the two integers that appear only once.
# Note: Return the two numbers in ascending order.
def single_number(A):
  xor = 0     # the result of a xor b
  grA = 0
  grB = 0
  for x in A:
    xor ^= x
  mask = (xor & (xor - 1)) ^ xor  # the last bit that a differs from b
  for x in A:
    # based on the last bit, group the items into groupA (include a) and groupB
    if x & mask:
      grA ^= x
    else:
      grB ^= x  
  lst = [grA, grB]
  lst.sort()
  return lst
# print(single_number([1, 2, 3, 1, 2, 4]))

## Maximum Satisfaction
# Given an array of integers A of size N denoting the quality of the fruits. A[i] represents the fruit quality of the ith fruit. Shaun needs to pick four fruits, but he needs to pick them so that his satisfaction value will be maximum.
# If a, b, c, and d are fruit quality of the four fruits picked, then the satisfaction value(a, b, c, d) = (a & b & c & d) where & is bitwise AND operator. Find the maximum satisfaction value Shaun can obtain.
def max_satisfaction(arr):
  i=31    #assuming input integer won't be greater than pow(2,32).
  ans=0
  while i>=0:
    count = 0
    for x in arr:
      if x&((1<<i)|ans)==(1<<i)|ans: #check if ith bit in the array is 1 or not
        count +=1
    if count > 3:
      ans += pow(2, i)
    i -= 1
  return ans
# A = [8,15,15,15,7]
# print(max_satisfaction(A))

#readable solution
def check(x, A):
  ct = 0
  for a in A:
    if (a & x) == x:
      ct += 1
    if ct > 3:
      return 1
  return 0
def solve(A):
  ans = 0
  for i in range(32, -1, -1):
    temp = ans | (1 << i)
    if check(temp, A) == 1:
      ans = temp
  return ans
# Solution Approach for above problem:
# Numbers up to 2*10pow9 can be represented in a 32-bit binary system. So as we want the largest answer, we will start traversing from the most significant bit and check whether this bit, 
# along with the bits set in the previous answer, is set in at least four numbers. If possible, we add corresponding power of two to the answer. 
# Similarly, we will do this for each bit in decreasing order and update the answer accordingly. 

## Bit Compression
# Richard Hendricks, a mastermind in compression algorithms, is an employee of Hooli in Silicon Valley. One day, he finally decided to quit and work on his new idea of the middle-out compression algorithm.
# He needed to work at the bit - level to compress data. He, eventually, encountered this problem. There is an array A of N integers. He has to perform certain operations on the elements.
# In any one operation, two indices i and j (i < j) are chosen, and A[i] is replaced with A[i] & A[j], and A[j] is replaced with A[i] | A[j], where & represents the Bitwise AND operation and | represents the Bitwise OR operation.
# This operation is performed over all the pairs of integers in the array. Help Richard find the Bitwise XOR of all the elements after performing the operations.
def bit_compression(arr):
  ans = 0
  for x in arr:
    ans ^= x
  return ans