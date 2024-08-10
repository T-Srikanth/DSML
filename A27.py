# DSML Advanced: Python Refresher 2
###################################################
######### Reference links #########
# https://hackmd.io/@scaler-topics-main/HyJvtfpy9
####################################################

## Reverse the dictionary
# You are given an integer T (Number of test cases). For each test case, You are given a dictionary as input,
#  reverse the dictionary (make the keys as values and values as keys), and return the inverted dictionary.
def reverse_dict(A):
  res = {}
  for key,value in A:
    res[value] = key
  return res
#OR
def invert_dict(data):
  inv_dict = dict(zip(data.values(), data.keys()))
  return inv_dict

## Most Frequent Element
# You are given T test cases. For each test case, you are given a list as an input. Complete the function to find the most frequent element in the list and return it.
# The most frequent element is the element occurs in the list the most number of times.
# Note: It is guaranteed that there will be only one unique element with the highest frequency in the list of inputs.
def most_frequent(A):
  res = {}
  max_count = 0
  ans = None
  for elem in A:
    if elem in res:
      res[elem] += 1
    else:
      res[elem] = 1
  for key in res.keys():
    if res[key]>max_count:
      max_count=res[key]
      ans = key
  return ans
# print(most_frequent(['Hii' ,'Hello' ,'Hii']))

## Map. reduce and filter
# In this exercise, you are given a function, and given ints, names, numbers as the input.
# Use map to return the list of the square of each numbers.
# Use filter to return the list with only the names that are less than or equal to seven letters.
# Use reduce to return the product of these numbers.
from functools import reduce
def func(ints,names,numbers):
  map_result = list(map(lambda x: x*x, ints))
  filter_result = list(filter(lambda x: len(x)<8,names))
  reduce_result = reduce(lambda x,y: x*y,numbers)
  return map_result, filter_result, reduce_result
# ints = [4, 6, 3, 9, 2, 8, 12]
# names = ["scaler", "interviewbit", "rishabh", "student", "course"]
# numbers = [4, 6, 9, 23, 5]
# print(func(ints, names,numbers))

## Email Validation
# You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
# Valid email addresses must follow these rules:
# It is of the form user@domain. user or domain can't be empty
# It must have the single @ in the address.
# The maximum length of the name before the @ is 20.
def valid_emails(A):
  result = list(filter(myfunc,A))
  return sorted(result)
def myfunc(string): #takes a string and returns True if it is a valid email
  tmp_lst = string.split("@")
  if len(tmp_lst)!=2:
    return False
  user, domain = tmp_lst[0], tmp_lst[1]
  if len(user)>20 or len(user)==0 or len(domain)==0:
    return False
  return True
# A=["sara@scaler.com","brian-23@scaler.com","brute_54@scaler.com"]
# print(valid_emails(A))


## Unique words
# You are given a string as input. You have to find the number of words that have unique characters in it
# (i.e. no single character is repeated) and length of the word must be greater than 3.
def unique_words(string):
  l = string.lower().split(" ")
  ans = 0
  for word in l:
    if len(word)==len(set(word)) and len(word)>3:
      ans += 1
  return ans
# S="the fruits of the tree were basically oranges and apples"
# print(unique_words(S))

## Fill the Data
# Complete the function, which accepts a string consisting of some numbers and blanks (underscores), separated by commas, and fills these blanks as per the given conditions:
#   blanks to the left of a number should be filled by the number distributed equally, into the number of blanks to the left, along with the number position itself
#   middle blanks of two numbers should be filled by their sum equally distributed, along with their two positions
#   right blanks of a number should be again distributed equally by that number, along with the position of the number itself.
def data_distribute(input_data):
  arr = input_data.split(",")
  u_count = 0
  right_num = 0
  left_num = 0
  for i in range(len(arr)):
    if arr[i] == '_':
      u_count += 1
    else: 
      right_num = int(arr[i])       
      if left_num!=0 and right_num!=0: # to handle underscores in the middle
        val = (left_num+right_num)//(u_count+2)
        for ind in range(i-u_count-1,i+1):
          arr[ind] = val
        right_num = 0
      else: # to handle underscores at the start and end
        val = (left_num+right_num)//(u_count+1)
        for ind in range(i-u_count,i+1):
          arr[ind] = val
      u_count = 0
      left_num = val
  if arr[-1] == '_': # to handle case where string ends with underscore '_'
    last_num_ind = None
    for ind in range(len(arr)):
      if arr[ind] == '_':
        last_num_ind = ind - 1
        break
    for i in range(last_num_ind,len(arr)):
      arr[i] = left_num//(u_count+1)
  return arr
# inp = '_,_,_,24'
# print(data_distribute(inp))
#OR
def data_distribute(input_data):
  filled_data = None
  # Splitting the data on the basis of ',' so that we can separately get the blanks(_) and the numbers.
  filled_data = input_data.split(',')
  # Intialising a position variable to keep a track at which index we are at while iterating
  pos = 0
  # Looping until there are '_' in the data
  while('_' in filled_data):
    # Intialising count variable to count the number of blanks we encounter before getting a number
    count = 0
    # Intialising a variable to store the sum till we encounter another number
    acc = 0
    # Iterating through the entire input
    for i in range(pos,len(filled_data)):
        count +=1
        # If the data is not a blank we simply add the value to the acc variable
        if filled_data[i] != '_':
            acc+=int(filled_data[i])
            # If the count is greater than 1 we break out from the for loop because it signifies we have got the second number
            # this condition is important for dealing blanks between 2 numbers
            if(count >1):
                break        
    # After we break out of loop we need to distribute the sum in the blanks. So we divide it by the count
    acc = acc//count        
    # We fill the position from the starting position to the position where we broke out from loop with the value of acc
    filled_data[pos:pos+count]= [acc]*count
    # Update the position of pos to start from the position where the loop broke out.
    pos = pos + count-1
  # Returning the required array
  return filled_data


    