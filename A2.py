# Time complexity - 1
###################################################
######### Reference links ######### 
# Understanding log : https://www.mathsisfun.com/algebra/logarithms.html
# AP: https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
# GP: https://www.mathsisfun.com/algebra/sequences-sums-geometric.html

# Extra Reading material on Time complexity : 
# https://medium.com/@abdurrafeymasood/understanding-time-complexity-and-its-importance-in-technology-8279f72d1c6a
# https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/

# How to deal with TLEs :
# https://www.geeksforgeeks.org/overcome-time-limit-exceedtle/
####################################################

def solve():
   for i in range(n):
        for j in range(i // 2):
            # O(1) operation
            print(j)
## time complexity of the above code is - O(N*N)

k = 0
for i in range(n//2, n+1):
    j = 2
    while j<=n:
         k = k + n//2
         j = j * 2
## time complexity of the above code is - O(NlogN)

a = 0
i = N
while i > 0:
    a += i
    i //= 2
## time complexity of the above code is  - O(logN)

## The complexity of Binary search algorithm is - O(logN) 

## If an algorithm has a time complexity of O(1), then the complexity of it is ? - constant

## If for an algorithm time complexity is given by O(log2n) then complexity will be - logarithmic time complexity

## If an algorithm has a time complexity of O(n), then the complexity of it is ? - linear

## If for an algorithm time complexity is given by O((3/2)^n) then complexity will be - exponential

def solve():
   i = n
   while i>0:
       if i%2==0:
            for j in range(1,n*n+1,2):
                 #O(1) operation
                 print(j)
       i = i//2
## time complexity of the above code is - O(N*NlogN)

