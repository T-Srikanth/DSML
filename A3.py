# Time complexity - 2
###################################################
######### Reference links ######### 
# 1. https://facultyweb.cs.wwu.edu/~wehrwes/courses/csci241_20s/lectures/L08/runtime_practice.pdf
# 2. https://www.happycoders.eu/algorithms/big-o-notation-time-complexity/
# 3. https://medium.com/@manishsundriyal/overview-time-space-complexity-f973513b701e
# 4. Asymptotic Notation Cheatsheet: https://www.codecademy.com/learn/asymptotic-notation-and-big-o-js/modules/asymptotic-notation-js/cheatsheet
####################################################

## An algorithm consists of two independent piece of code, having complexities f(n) and g(n) respectively.
# What would be the complexity of the complete algorithm - MAX( f(n), g(n) )

## To measure Time complexity of an algorithm Big O notation is used which: - describes limiting behaviour of the function,
# characterises a function based on growth of function, upper bound on growth rate of the function (multiple correct answers)

## What will be the Time Complexity of the given code? - O(n^2)
def solve():
    i = 1
    while (i < n):
        x = i
        while (x > 0):
            #O(1) operation
            x -= 1
        i += 1

## What is the time complexity of the following code snippet? - O(n^2)
i = 0
while i*i <= N:
    for j in range(N+1):
        for k in range(N+1):
            i += 1
            #O(1) operation

    i += 1
# After the first iteration, i becomes (N+1)^2 +1, This means after the first iteration, i is very large, specifically larger than N
# Hence the while loop runs only once in practice

## What is the time complexity of the following code snippet? - O(n^2)
for i in range(3, n/3, 3):
    for j in range(2, n/2, 2):
        # O(1) operation
        print(j)

## Find the Time Complexity of the following function solve : - O(4^N)
def solve(N):
    for i in range(2 ** N):
        j = i
        while j > 0:
            j -= 1

## What is the time complexity of the following code snippet? - O(√n)
def fun():
    i = 1
    while(i * i <= n):
        j = 1
        while(j * j <= i):
            # O(1) operation
            j += i
        i += 1 
# Inner loop will run only for j = 1, as for the next iteration j is incremented by i which will 
# fail the condition of j^2 < i. So the time complexity is proportional to that of the outer loop which is O(√n)
