# DSML Advanced: Python Refresher 1
###################################################
######### Reference links #########
####################################################

## Electricity Bill
# Given an integer A denoting the amount of units of electricity consumed, you have to calculate the electricity bill (in Rs.) with the help of the below charge conditions:
#     For first 50 units Rs. 0.50/unit
#     For next 100 units Rs. 0.75/unit
#     For next 100 units Rs. 1.20/unit
#     For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.
# Note: As the electricity bill can have any real value (floating point), you have to tell the floor value of the bill.
# Floor value of a floating point is the closest integer less than or equal to that value. For eg, Floor value of 2.91 is 2.
def bill(A):
  ans = None
  amt = 0
  if A <= 50:
    amt = A*0.50
  elif A <= 150:
    amt = 25 + (A-50)*0.75
  elif A <= 250:
    amt = 100 + (A-150)*1.20
  else:
    amt = 220 + (A-250)*1.50
  ans = amt + amt*0.20
  return int(ans)

## Merge 2 Sorted
# You are given an integer T (Number of test cases). For each test case, You are given two sorted arrays A and B. You have to merge the given arrays into a single sorted array.
def merge(A, n1, B, n2): # A and B are arrays and n1, n2 are their respective lengths 
  C = [0] * (n1 + n2)
  ptrA = 0
  ptrB = 0
  ptrC = 0
  while ptrA < n1 and ptrB < n2:
    if A[ptrA] <= B[ptrB]:
      C[ptrC] = A[ptrA]
      ptrC += 1
      ptrA += 1
    else:
      C[ptrC] = B[ptrB]
      ptrC += 1
      ptrB += 1
  while ptrA < n1:
    C[ptrC] = A[ptrA]
    ptrC += 1
    ptrA += 1
  while ptrB < n2:
    C[ptrC] = B[ptrB]
    ptrC += 1
    ptrB += 1
  return C
