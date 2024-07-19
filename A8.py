# Arrays - 2D Matrices
###################################################
######### Reference links #########
####################################################

## Add the matrices
# You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
# Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.
def add_matrices_row(A, B):
  rows = len(A)
  columns = len(A[0])
  res = [[0]*columns for i in range(rows)]
  for i in range(rows):
    for j in range(columns):
      res[i][j] = A[i][j] + B[i][j]
  return res
# A = [[1, 2, 3],   
#      [4, 1, 2],   
#      [7, 8, 9]]  

# B = [[9, 9, 7],   
#      [1, 2, 4],   
#      [4, 6, 3]]
# print(add_matrices_row(A,B))

## Column Sum
# You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.
def add_matrices_col(A):
  rows = len(A)
  columns = len(A[0])
  res = [0]*columns
  for j in range(columns):
    for i in range(rows):
      res[j] += A[i][j]
  return res
# A =[[1,2,3,4],
#     [5,6,7,8],
#     [9,2,3,4]]
# print(add_matrices_col(A))

## Matrix Multiplication
# You are given two integer matrices A(having M X N size) and B(having N X P). You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).
def multiply_matrices(A, B):
  res_rows = len(A)
  res_columns = len(B[0])
  col_A = row_B = len(A[0])
  res = [[0]*res_columns for i in range(res_rows)]
  for i in range(res_rows):
    for j in range(res_columns):
      for k in range(col_A):
        res[i][j] += A[i][k]*B[k][j]  ## Multiplying A[i][k] by B[k][j] and adding that to res[i][j]
  return res
# A = [[1, 2],
#      [3, 4]]
# B = [[5, 6],
#      [7, 8]]
# print(multiply_matrices(A,B))

## Anti Diagonals
# Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
# Input: A = [[1 2 3],[4 5 6],[7 8 9]] ; Output: B = [[1 0 0],[2 4 0],[3 5 7],[6 8 0],[9 0 0]]
# A =[[00,01,02],
#     [10,11,12],
#     [20,21,22]]
def anti_diagonals(A):
  size_A = len(A)
  res_rows = size_A*2 - 1
  res_cols = len(A)
  res = [[] for i in range(res_rows)]
  for i in range(size_A):
    for j in range(size_A):
      res[i+j].append(A[i][j])
  for i in range(res_rows):
    while (len(res[i])<res_cols):
      res[i].append(0)
  return res
# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(anti_diagonals(A))

## Matrix Transpose
# Given a 2D integer array A, return the transpose of A. The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
def transpose_matrix(A):
  res_rows = len(A[0])
  res_cols = len(A)
  res = [[0]*res_cols for i in range(res_rows)]
  for i in range(res_rows):
    for j in range(res_cols):
      res[i][j] = A[j][i]
  return res
# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(transpose_matrix(A))

## Matrx Subtraction
# You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M). You have to subtract matrix B from A and return the resultant matrix. (i.e. return the matrix A - B).
# If A and B are two matrices of the same order (same dimensions). Then A - B is a matrix of the same order as A and B and its elements are obtained by doing an element wise subtraction of A from B.
def sub_matrices(A,B):
  rows = len(A)
  columns = len(A[0])
  res = [[0]*columns for i in range(rows)]
  for i in range(rows):
    for j in range(columns):
      res[i][j] = A[i][j] - B[i][j]
  return res
# A =  [[1, 2, 3], 
#       [4, 5, 6], 
#       [7, 8, 9]]

# B =  [[9, 8, 7], 
#       [6, 5, 4], 
#       [3, 2, 1]]
# print(sub_matrices(A,B))

## Matrix Scalar product
# You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.
def sub_matrices(A,B):
  rows = len(A)
  columns = len(A[0])
  for i in range(rows):
    for j in range(columns):
      A[i][j] *= B
  return A

## Row Sum
def row_sum(A):
  rows = len(A)
  columns = len(A[0])
  res = []
  for i in range(rows):
    sum = 0
    for j in range(columns):
      sum += A[i][j]
    res.append(sum)
  return res
# A = [[1,2,3,4],
# [5,6,7,8],
# [9,2,3,4]]
# print(row_sum(A))

## Row to Column Zero
# You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.
def row_column_zero(A):
  rows = len(A)
  columns = len(A[0])
  track = []
  for i in range(rows):
    for j in range(columns):
      if A[i][j] == 0:
        track.append({'i': i, 'j': j})
  for indexes in track:
    for key,value in indexes.items():
      if key == 'i':
        for col in range(columns):
          A[value][col] = 0
      if key == 'j':
        for row in range(rows):
          A[row][value] = 0
  return A
# A = [[1,2,3,4],
# [5,6,7,0],
# [9,2,0,4]]
# print(row_column_zero(A))

# OR
def solve(A):
  n = len(A)
  m = len(A[0])
  for i in range(0,n):
    flag = 0
    for j in range(0,m):
      if A[i][j] == 0:
        flag = 1
    if flag == 1:
      for j in range(0,m):
        if A[i][j] != 0:
          A[i][j] = -1
  for j in range(0,m):
    flag = 0
    for i in range(0,n):
      if A[i][j] == 0:
        flag = 1
    if flag == 1:
      for i in range(0,n):
        if A[i][j] != 0:
          A[i][j] = -1
  for i in range(0,n):
    for j in range(0,m):
      if A[i][j] == -1: A[i][j] = 0
  return A

# OR
def solve(A):
  rows = set()
  cols = set()
  for i in range(len(A)):
    for j in range(len(A[0])):
      if A[i][j]==0:
        rows.add(i)
        cols.add(j)
  for i in rows:
    for j in range(len(A[0])):
      A[i][j] = 0
  for j in cols:
    for i in range(len(A)):
      A[i][j] = 0
  return A

## Are Matrices same
# You are given two matrices A and B of equal dimensions and you have to check whether two matrices are equal or not.
# Note: Both matrices are equal if A[i][j] == B[i][j] for all i and j.
def equal_matrices(A,B):
  rows = len(A)
  columns = len(A[0])
  for i in range(rows):
    for j in range(columns):
      if A[i][j] != B[i][j]:
        return 0
  return 1
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = [[1, 2, 3],
#      [7, 8, 9],
#      [4, 5, 6]]
# print(equal_matrices(A,B))

## Minor Diagonal Sum
# You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
# Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).
# my solution
def minor_diagonal_sum(A):
  rows = len(A)
  columns = len(A[0])
  sum = 0
  for i in range(rows):
    for j in range(columns):
      if i+j == rows-1:
        sum += A[i][j]
  return sum
# A = [[3, 2],
#       [2, 3]]
# print(minor_diagonal_sum(A))

# better solution
def solve(self, A):
  N = len(A)
  sum = 0
  for i in range(0, N):
    sum += A[i][N - 1 - i]
  return sum

## Main Diagonal Sum
# You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
# Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.
def main_diagonal_sum(A):
  rows = len(A)
  sum = 0
  for i in range(rows):
    sum += A[i][i]
  return sum
