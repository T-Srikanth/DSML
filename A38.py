# DSML Intemediate: Coding Test
###################################################
######### Reference links #########
####################################################

## Is it isomorphic?
# Complete the function is_isomorphic() to check whether two strings are isomorphic or not. Two strings s1 and s2 are called isomorphic if the characters in s1 can be replaced to get s2
# Note: All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
def is_isomorphic(s1, s2):
  '''
  input:
  s1 -> the first string 
  s2 -> the second string
  
  output:
  True or False -> return True of False boolean values based on whether the two strings are isomorphic or not
  '''
  myDict = {}
  for i in range(len(s1)):
    if(s1[i] not in myDict):
      myDict[s1[i]] = s2[i]
    elif(myDict[s1[i]] != s2[i]):
      return False
  return True
# print(is_isomorphic("hello","cahho"))

## Is it a power of 3?
# Complete the function power_of_3() to check whether a number is power of 3 or not. Use recursion to solve this problem.
def power_of_3(n):
  '''
  input:
  n -> an integer
  output:
  True or False -> depending on whether the number is power of n or not
  '''
  if (n == 1):
    return True
  return power_of_3(n/3) if n%3==0 else False 
# print(power_of_3(11))

## Number of ones in sorted binary number
# You are given a binary sorted number i.e. a binary number where all the 1's come together after all the 0's example 3(0011) or 7(0111). Count the number of 1's that appear in number and display it,
# and do so in logn time.
def number_of_1s(num, left, right):
  '''
  input:
  num -> binary number in string format
  left -> initially 0, pointing to left index
  right -> initially len(num) - 1, pointing to right index
  output:
  count of number of 1s in the string
  '''
  left = 0               ## time complexity for this is O(n)
  right = len(num) - 1
  count = 0
  print(len(num))
  while left <= right +1:
    if(int(num[left])):
      print(len(num) - left)
      count = len(num) - left
      break
    elif(not int(num[right])):
      print(len(num) - right - 1)
      count = len(num) - right - 1
      break
    left  += 1
    right -= 1
  return count
# print(number_of_1s("0011",0,3))

def count_ones(num):      ##### Binary search, this has time complexity O(logn)
  left, right = 0, len(num) - 1
  while left <= right:
    mid = (left + right) // 2    
    if num[mid] == '1':
      # Move to the left to find the first '1'
      right = mid - 1
    else:
      # Move to the right to skip '0's
      left = mid + 1          
  # Left will now be at the index of the first '1'
  return len(num) - left