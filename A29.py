# DSML Advanced: Numpy 1
###################################################
######### Reference links #########
####################################################

## Return binary
# Given a Numpy array of integers as an input to the function binary(), complete the given function to convert each element in the array into its binary representation.
# For example: In binary, 5 => 101, 7 => 111, 10 => 1010.
# Note: You are not allowed to use the inbuilt bin() function and both input and output array have elements of datatype 'int'.
import numpy as np
def binary(arr):
  """
    arr is a NumPy array 
    return output array consisting of binary representation of each element
  """
  vec = np.vectorize(convert_to_bin)   #The vectorize() function is used to generalize function class.The vectorized function evaluates pyfunc (here func) 
  arr = vec(arr)                       #over successive tuples of the input arrays like the python map function, except it, uses the broadcasting rules of NumPy.
  return arr
def convert_to_bin(number):
  res = []
  while number>0:
    res.append(str(number%2))
    number = number//2
  ans = "".join(res[::-1])
  return int(ans)
# A = [[2,3,4], [5,6,7]]
# print(binary(A))

## Sorting in matrix
# You are a Teaching Assistant of the DSML course. You have access to every student’s marks in every quiz. The marks are stored in a matrix where matrix[i][j] represents the marks of the ith student 
# in the jth quiz. The course instructor wants you to sort the marks of students according to jth quiz in increasing order so that he can evaluate the performance of students in that particular quiz.
# Here, you have to create a python program using which the instructor can sort the data on the basis of a given column(quiz). The program will return the matrix with the marks sorted in jth quiz.
# The dimension of the input matrix is m× n, the output is expected to be a 2d numpy matrix of dimension mxn, but in the output the jth column must be arranged in the ascending order.
# Note: The input will be 2D list not array. First convert it to array.
def sort_marks(list2d, j):
  '''Input: arr2d= a 2d python list.
    j= integer representing the number of quiz according to which the marks need to be sorted.
    Output: a 2d numpy array.'''
  ans = None
  np_arr = np.array(list2d)
  c = np.argsort(np_arr[:,j-1])
  ans = np_arr[c,:]    
  return ans
# A = [[5 ,3 ,9],
# [2, 1, 4],
# [7, 6, 8]]
# print(sort_marks(A,2))

## Row-wise unique
# You are a developer for Scalar, and are tasked to write a program that can find the number of times a student has accessed a particular question.
# For this, you proposed that every time a student opens a question, the question’s id will be appended to the row representing the student’s id in a matrix. For example, if student i opens question j, 
# j will be appended to ith row of the matrix.For the prototype, we have limited the number of questions to 10 for consideration. So id of questions <=10. Return the matrix with the same number of rows(m) 
# as that of the input matrix, but this time matrix[i][j] should represent the number of times student i accessed question j. The output matrix is a 2d-numpy matrix of dimension (m*10).
def countfreq(arr2d):
  # Make sure that you are printing the output matrix simply inside this function.
  '''input: arr2d= a 2d python list
    output: a 2d numpy array'''            
  return np.array([func(row) for row in arr2d])
def func(row):
  uniq, count = np.unique(row, return_counts=True)
  zeros = np.zeros(10, dtype=int)
  zeros[uniq-1] = count
  return (zeros.astype(int))
# A = [[5 ,3 ,9],
# [2, 1, 4]]
# print(countfreq(A))