# Introduction to problem solving -DSA
## check if the given number is prime or not 
import math

def is_prime(A):
  factors = 0
  A_root = math.floor(math.sqrt(A))
  for i in range(1,A_root+1):
    if(A%i == 0):
      factors += 2
  if(factors == 2):
    print("Number is prime")
  else:
    print("Number is NOT prime")

number = int(input("enter number: "))
# is_prime(number)

############################################
## check if the given number is a perfect number or not.
## A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself).

def factors_of(B):
  divisors = []
  B_root = math.floor(math.sqrt(B))
  for i in range(1,B_root+1):
    if(B%i == 0):
      divisors.append(i)
      if(i != B/i):
        divisors.append(round(B/i))
  return divisors

def is_perfect(B):
  factors = factors_of(B)
  factors.sort()
  factors.pop()
  if(sum(factors) == B):
    print(B,"is a perfect number")
  else:
    print(B,"is NOT a perfect number")

# is_perfect(number)

############################################
## sum of first N natural numbers(from 1 to N)

def sum_N(C):
  return round(C*(C+1)/2)

# print(sum_N(number))

############################################
## Given a number D. Return square root of the number if it is perfect square otherwise return -1.

def is_perfect_square(D):
  if D < 0:
    return -1
  if D == 0 or D == 1:
    return D
  low, high = 1, D//2

  while low <= high:
    mid = (low + high)//2
    mid_squared = mid * mid

    if mid_squared == D:
      return mid
    elif mid_squared < D:
      low = mid + 1
    elif mid_squared > D:
      high = mid - 1
  return -1

# result = is_perfect_square(number)
# print(f"The square root of {number} is {result}" if result != -1 else f"{number} is not a perfect square")
# print("The square root of {} is {}".format(number,result) if result != -1 else "{} is not a perfect square".format(number))

############################################
## You are given an integer E you need to print all the Armstrong Numbers between 1 to E. (E inclusive).
# If sum of each digit raised to the power of (number of digits) of the number is equal to the number itself, then the number is called an Armstrong number.

#A^2 + B^2 = AB
# A^3 + B^3 + C^3 = ABC
def is_armstrong(E):
  digits = str(E)
  num_digits = len(digits)
  exp = sum(int(digit)**num_digits for digit in digits)
  return exp == E

def print_armstrong_numbers(E):
  for num in range(1, E+1):
    if is_armstrong(num):
      print(num)

# print_armstrong_numbers(number)

############################################
##Take a number F as input, print its multiplication table having the first 10 multiples.

def print_mul_table(F):
  for i in range(1, 11):
    print("{} * {} = {}".format(F, i, F*i))

# print_mul_table(number)