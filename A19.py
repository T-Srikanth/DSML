# Intermediate DSA: Recursion - 2
###################################################
######### Reference links #########
####################################################

## Implement Power Function
# Implement pow(A, B) % C. In other words, given A, B and C, Find (AB % C).
# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.
def power(A,B,C):
  if B==0:
    return 1
  x = power(A,B//2,C)
  if B%2 == 0:
    return (x*x)%C
  else:
    return (A*(x*x)%C)%C
# A = 0
# B = 4
# C = 1
# print(power(A,B,C))

## Sum of digits
# Given a number A, we need to find the sum of its digits using recursion.
def sum_digits(A):
  if A==0:
    return 0
  return A%10 + sum_digits(A//10)
# A = 11
# print(sum_digits(A))

## Is magic?
# Given a number A, check if it is a magic number or not. A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the 
# sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.
def is_magic(A):
  if A<10:
    return 1 if A==1 else 0
  digit_sum = 0
  while A > 0:
    digit_sum += A%10
    A //= 10
  return is_magic(digit_sum)
# A = 1291
# print(is_magic(A))

## Kth Symbol
# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).
def kth_symbol(A,B):
  # Base case: first row always has a single '0'
  if A==1:
    return 0
  # Find the length of the previous row
  mid=(2**(A-1))/2
  # If B is in the first half, it mirrors the previous row
  if B<=mid:
    return kth_symbol(A-1,B)
  # If B is in the second half, it's the complement of the corresponding first half
  else:
    return 1-kth_symbol(A-1,B-mid)
# A = 2
# B = 2
# print(kth_symbol(A,B))
#OR
def solve(N,K):
  def Grammar(N,K):
    if N==1:
      return 0
    if K%2==0:
      if Grammar(N-1,K/2) == 0:
        return 1
      else:
        return 0
    else:
      if Grammar(N-1,(K+1)/2) == 0:
        return 0
      else:
        return 1
  return Grammar(N,K)
  
## Gray Code
# The gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer A representing the total number of bits in the code, 
# print the sequence of gray code. A gray code sequence must begin with 0.
def grayCode(n):
  # Base case: for 0 bits, only one gray code exists which is [0]             #Note the following :
  if n == 0:                                                                  #Let G(n) represent a gray code of n bits.
    return [0]                                                                #Let R(n) denote the reverse of G(n).
  # Generate the gray code sequence for n bits                                #Note that we can construct.
  result = []                                                                 #G(n+1) as the following :
  num_codes = 1 << n  # There are 2^n gray codes for n bits                   #0G(n)
  for i in range(num_codes):                                                  #1R(n)
    gray = i ^ (i >> 1)                                                       #Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
    result.append(gray)                                                       #Note that the last element of G(n) and the first element of R(n) are the same. So the above sequence is valid.
  return result                                                               #Example G(2) to G(3) :
A=3                                                                           #0 00
print(grayCode(A))                                                            #0 01
                                                                              #0 11
                                                                              #0 10
                                                                              #1 10
                                                                              #1 11
                                                                              #1 01
                                                                              #1 00

