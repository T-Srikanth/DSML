# DSML Advanced: Numpy 2
###################################################
######### Reference links #########
####################################################

## Convert into One Hot Encoding
# Given a 1D NumPy array containing integers, convert each integral value into one-hot encoded values.
# In the One Hot Encoding technique, each integer value is represented as a binary vector that is all 0s except the index of the integer which is marked as 1.
# Note: Input and output arrays are of dtype 'int'.
# example: for input array [1,3,4,1,2]; output should be array [[0,1,0,0,0],  [0,0,0,1,0],  [0,0,0,0,1],  [0,1,0,0,0],  [0,0,1,0,0]] 
import numpy as np
def covert__to_one_hot(arr):
  result = np.zeros((arr.size,arr.max()+1),dtype=int) #creates a n*m matrix of zeroes where n is size of input array and m is max of input + 1
  result[np.arange(arr.size),arr] = 1 #access the coordinates of the matrix and sets the value to 1
  return result
# test = np.array([1,3,4,1,2])
# print(covert__to_one_hot(test))

## Original Matrix Retrieval
# John and Edo have been childhood friends. Both love playing with numbers, especially with matrices. One day, John comes up with an interesting problem for Edo. He takes a 4 x 4 matrix, and breaks it down into 4 parts, top left, top right, bottom left, and bottom right, and now wants Edo to retrieve the original matrix from some hints about the 4 parts. In detail,
# 1. For each part, Edo will be given 2 numbers, and he has to generate 4 spaced equal numbers between these 2 numbers (both numbers included).
# 2. After generating this 4 length array, convert it into a 2x2 matrix, and merge them as per requirement (according to their positions).
# example: for input [(0,2),(5,7),(1,3),(6,9)] output is [[0.  0.7 5.  5.7], [1.3 2.  6.3 7. ], [1.  1.7 6.  7. ], [2.3 3.  8.  9. ]]
def combine(inpt_lis):
  '''input: inpt_lis- Its a list of length of 4 and contains tuples.
    Output: A 2d-numpy array is expected to be returned'''      
  ans=None
  left_top = np.round(np.linspace(inpt_lis[0][0],inpt_lis[0][1],4),decimals=1).reshape(2,2)
  right_top = np.round(np.linspace(inpt_lis[1][0],inpt_lis[1][1],4),decimals=1).reshape(2,2)
  left_btm = np.round(np.linspace(inpt_lis[2][0],inpt_lis[2][1],4),decimals=1).reshape(2,2)
  right_btm = np.round(np.linspace(inpt_lis[3][0],inpt_lis[3][1],4),decimals=1).reshape(2,2)
  top = np.append(left_top,right_top,axis=1)
  btm = np.append(left_btm,right_btm,axis=1)
  ans = np.append(top,btm,axis=0)
  return ans
# print(combine([(0,2),(5,7),(1,3),(6,9)]))

## Trial Softmax
# The softmax function is used in machine learning algorithms for classification applications. What it basically does is that it takes input as an array and 
# converts it into a probability distribution where the sum of each elements' probability will be 1.
# Write a function that could take a list as an input and can return a NumPy array that would have the softmax scores of each element as a member.
def softmax(arr):
  np_arr =np.array(arr)
  denominator = np.sum(np.exp(np_arr))
  result = np.exp(np_arr)/denominator
  return np.round(result,decimals=3)
# print(softmax([6,2,4,3,1]))
#OR
def softmax(data):
  x=np.asarray(data)
  e_x = np.exp(x)
  return (np.round(e_x / e_x.sum(),3))
