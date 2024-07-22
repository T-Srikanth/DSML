# Bit Manipulations - 1
###################################################
######### Reference links #########
####################################################

## Single number
# Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
def single_number(A):
  n = len(A)
  res = A[0]
  for i in range(1,n):
    res ^= A[i]  #XOR operation - XOR of any number with itself is zero and XOR of any number with 0 is the number itself
  return res

## Add Binary Strings
# Given two binary strings A and B. Return their sum (also a binary string).
def get(x):
  if x == 0:
    return '0'
  if x == 1:
    return '1'
def binary_sum(A,B):
  len_A = -len(A)
  len_B = -len(B)
  big_len = min(len_A,len_B)
  carry = 0
  ans = ''
  for i in range(-1, big_len-1, -1):
    if i>=len_A and i>=len_B:
      val = ord(A[i])+ord(B[i]) - 2*ord('0')+carry
      carry = val//2
      val -= 2*carry
      ans += get(val)
    elif i>=len_A:
      val = ord(A[i]) - ord('0')+carry
      carry = val//2
      val -= 2*carry
      ans += get(val)
    else:
      val = ord(B[i]) - ord('0')+carry
      carry = val//2
      val -= 2*carry
      ans += get(val)
  if carry == 1:
    ans += '1'
  return ans[::-1]
# A = "100"
# B = "11"
# print(binary_sum(A,B))

## Number of 1 Bits
# Write a function that takes an integer and returns the number of 1 bits present in its binary representation.
def ones_count(A):
  count = 0
  res = 0
  while A>=1:
    res = A%2
    A = A//2
    if res == 1:
      count += 1
  return count
# print(ones_count(6))

#OR
def numSetBits(self, A):
  ret = 0
  while A != 0:
    # rightmost set bit of A becomes unset by performing 'A & (A-1)' operation each time the loop runs until all the set bit are unset making A == 0
    A = A & (A - 1)
    ret += 1
  return ret

## Interesting Array
# You have an array A with N elements. We have two types of operation available on this array :
#   We can split an element B into two elements, C and D, such that B = C + D.
#   We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
# You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0 after several splits and/or merge?
def interesting_array(arr):  #if there even count of odd numbers in the given array then it is possible 
  n = len(arr)
  odd_count = 0
  for i in range(n):
    if arr[i]%2:
      odd_count += 1
  if odd_count%2 == 0:
    return 'YES'
  else:
    return 'NO'
# A = [9]
# print(interesting_array(A))

## Reverse Bits
# Reverse the bits of an 32 bit unsigned integer A.
def reverse(A):
  i = 31
  ret = 0
  while i >= 0:
    temp = ((A & 1<<i) >> i)&1   ## (binary '>>' i) operation moves the binary value on the left side of it i places to the right and '<<' moves it left side.
    ret = ret | temp << (31-i)  ## The function iterates through each bit of the 32-bit integer A. It extracts each bit and places it in its mirrored position in the result ret.
    i -= 1
  return ret
# print(reverse(3))