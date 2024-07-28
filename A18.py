# Intermediate DSA: Recursion - 1
###################################################
######### Reference links #########
####################################################

## Check Palindrome using recursion
# Write a recursive function that checks whether string A is a palindrome or Not.Return 1 if the string A is a palindrome, else return 0.
# Note: A palindrome is a string that's the same when read forward and backward.
def solve_p(A):
  # Assume is_pal(A) returns True if A is pal
  def is_pal(A,s,e):
    if s>=e:
      return 1
    if A[s]==A[e]:
      return is_pal(A,s+1,e-1)
    return 0
  
  start=0
  end=len(A)-1
  return is_pal(A,s=start,e=end)
# A = "namqman"
# print(solve_p(A))

## Find Fibonacci 
# The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation: Fn = Fn-1 + Fn-2
# Given a number A, find and return the Ath Fibonacci Number using recursion. Given that F0 = 0 and F1 = 1.
def fibo(A):
  if A <= 1:
    return A
  return fibo(A-1)+fibo(A-2)
# A = 9
# print(fibo(A))

## Find Factorial!
# Write a program to find the factorial of the given number A using recursion.
# Note: The factorial of a number N is defined as the product of the numbers from 1 to N.
def factorial(A):
  if A<=1:
    return 1
  return factorial(A-1)*A
# A = 0
# print(factorial(A))

## Print reverse string
# Write a recursive function that takes a string, S, as input and prints the characters of S in reverse order.
def solve_reverse(S):  
  def reverse_list(A,s,e):
    if s>e:
      return A
    A[s],A[e]=A[e],A[s]
    return reverse_list(A,s+1,e-1)
  A=list(S)
  reversed_list = reverse_list(A,0,len(A)-1)
  return ''.join(reversed_list)
# S='cool'
# print(solve_reverse(S))

## Sum of Digits!
# Given a number A, we need to find the sum of its digits using recursion.
def solve_sum(A):
  def sum_of_digits(A,i):
    if i==len(A):
      return 0
    return int(A[i])+sum_of_digits(A,i+1)

  str_list = list(str(A))
  sum = sum_of_digits(str_list,0)
  return sum
# A = 11
# print(solve_sum(A))
#OR
def sum_of_digit( n ): 
    if n == 0: 
        return 0
    return (n % 10 + sum_of_digit(int(n / 10))) 

def solve(A):
  return sum_of_digit(A)