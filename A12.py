# Maths - Modular Arithmetic Intro
###################################################
######### Reference links #########
####################################################

## Excel Column Number
# Given a column title as appears in an Excel sheet, return its corresponding column number.
# AB should output 28; ord('A')=65; A should output 1, B should output 2 ... Z should output 26 then AA should output 27
def col_number(string):
  ans = 0
  n = len(string)
  for i in range(n):
    ans += (ord(string[i])-ord('A')+1)*pow(26,n-i-1)
  return ans

#OR
def titleToNumber(A):
  n = len(A)
  A = A[::-1]  # reverse the string
  ret = 0
  # traverse each character
  for i in range(n):
    ret += (26 ** (i)) * (ord(A[i]) - ord('A') + 1)
  return ret
# print(col_number('AB'))

## A,B and Modulo
# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.
def solve(A,B):
  return abs(A-B)

## Divisibility by 8
# You are given a number A(input in string format) in the form of a string. Check if the number is divisible by eight or not. Return 1 if it is divisible by eight else, return 0.
# Note: for a number to be divisible by 8, its last 3 digits should be divisible by 8
def divisible_8(A):
  n = len(A)
  s = ""
  if n <= 3:
    s = A
  else:
    s = A[n-3] + A[n-2] + A[n-1]
  num = int(s)
  if num%8 == 0:
    return 1
  return 0


## Mod String
# You are given a large number in the form of a string A where each character denotes a digit of the number.
# You are also given a number B. You have to find out the value of A % B and return it.

# (a * b) mod x = [(a mod x) * (b mod x)] mod x
# (a + b) mod x = [(a mod x) + (b mod x)] mod x
# We can represent a number "abcd" as (a * 1000) + (b * 100) + (c * 10) + (d * 1).
def mod_string(A,B):
  n = len(A)
  A = A[::-1]
  mod_ans = 0
  for i in range(n):
    temp = (int(A[i])%B)*(pow(10,i)%B)
    mod_ans = (mod_ans+temp)%B
  return mod_ans
# A = "2322424545435"
# B = 43
# print(mod_string(A,B))

## Concatenate three numbers
# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.
# Return the minimum result obtained.
def solve(A, B, C):
  return int(''.join([str(x) for x in sorted([A, B, C])]))

## Find if two rectangles overlap
# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
# For the First rectangle,
#   Bottom left corner is (A, B)           problem constraints:      -104 <= A < C <= 104
#   Top right corner is (C, D)                                       -104 <= B < D <= 104
# For the Second rectangle,                                          -104 <= E < G <= 104
#   Bottom left corner is (E, F)                                     -104 <= F < H <= 104
#   Top right corner is (G, H). 
# Find and return whether the two rectangles overlap or not.
# Hint: First, we can see if a foot of one rectangle is >= top of another rectangle, then an answer is not possible. You can make a similar argument about the y-axis.
def overlap(A,B,C,D,E,F,G,H):
  if A>=G or E>=C:
    return 0
  if F>=D or B>=H:
    return 0
  return 1

## Leap year?
# Given an integer A representing a year, Return 1 if it is a leap year else, return 0.A year is a leap year if the following conditions are satisfied:
#   The year is multiple of 400.
#   or the year is multiple of 4 and not multiple of 100.
def leap_year(A):
  if (A%400)==0 or ((A%4==0)and(A%100!=0)):
    return 1
  return 0
# print(leap_year(1999))

## Least common multiple
# Write a program to input an integer T and then for each test case input two integers A and B in two different lines and then print T lines containing Least Common Multiple (LCM) of two given 2 numbers A and B.
# Note: LCM of two integers is the smallest positive integer divisible by both.
# Hint: GCD of two numbers always exists between 1 and minimum among the two numbers and LCM = (A * B) / GCD
def lcm(A,B):
  gcd = 1
  for i in range(1, min(A,B)+1):
    if A%i==0 and B%i==0:
      gcd = i
  lcm = (A*B)//gcd  # using // to get integer output
  return lcm
# print(lcm(2,3))
