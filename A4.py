# Intro to Arrays
###################################################
######### Reference links ######### 
# Learn Lists in Python: https://github.com/scaleracademy/intro-to-python/blob/master/lecture3.md
# Python Practice: https://py.checkio.org/
# Python Lists Cheatsheet: https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-lists/cheatsheet
# Python Books: https://github.com/vinta/awesome-python#books
###################################################

## Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.
# example input: arr = [1, 2, 3, 4], B = 2; output: arr = [3, 4, 1, 2]
def reverse(A, start, end):
    i, j = start, end
    while(i < j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i, j = i + 1, j - 1

def main():
    temp = input().split()
    N = int(temp[0])
    A = [0] * N
    for i in range(1, N + 1):
        A[i - 1] = int(temp[i])
    B = int(input())
    B = B % N
    reverse(A, 0, N - 1)
    reverse(A, 0, B - 1)
    reverse(A, B, N - 1)
    for i in range(0, N):
        print(A[i], end = ' ')
    print()
    return 0

# if __name__ == "__main__":
#     main()
# or use the below code
def rotate_array_right(A, B):
    N = len(A)
    B = B % N  # Effective rotations
    return A[-B:] + A[:-B]  # Rotate array by slicing

def main():
    A = list(map(int, input("Enter the array elements separated by space: ").split()))
    B = int(input("Enter the number of rotations: "))
    result = rotate_array_right(A, B)
    print("Array after rotating", B, "times to the right:")
    print(result)
# if __name__ == '__main__':
#     main()

## Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
def check_good_pair(arr, B):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if(arr[i]+arr[j]==B):
                return True
    return False

## Take input an array A of size N and write a program to print maximum and minimum elements of the input. The only line of the input would contain a single integer N that represents the length of the array followed by the N elements of the input array A.
def max_and_min(arr):
    maxi, mini = arr[0], arr[0]
    n = len(arr)
    for i in range(n):
        if(arr[i]>maxi):
            maxi = arr[i]
        if(arr[i]<mini):
            mini = arr[i]
    print(maxi)
    print(mini)

## You are given a constant array A. You are required to return another array which is the reversed form of the input array.
def reverse_arr(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    print(arr)

## You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
def solve(A):
    # This loop calculates the largest element in the list.
    max_elem = -1
    for x in A:
        if x > max_elem:
            max_elem = x
    
    # This loop calculates the second largest element in the list.   
    second_max = -1
    for x in A:
        if x > second_max and x != max_elem:
            second_max = x
    return second_max

##  You are given an integer T denoting the number of test cases. For each test case, you are given an integer array A. You have to print the odd and even elements of array A in 2 separate lines.
# Note: Array elements should have the same relative order as in A.
def main():
    T = int(input())

    while T > 0:
        N = int(input())
        A = [0] * N
        cnto = 0
        cnte = 0
        A = input().split()
        
        for i in range(0, N):
            A[i] = int(A[i])
            if A[i] % 2 == 1:
                cnto += 1
            else:
                cnte += 1
        B = [0] * cnto
        C = [0] * cnte
        ptrB = 0
        ptrC = 0
        # looping from 0 to N-1
        for i in range(0, N):
            if A[i] % 2 ==  1:
                B[ptrB] = A[i]
                ptrB += 1
            else:
                C[ptrC] = A[i]
                ptrC += 1
        # looping over count of odd integers
        for i in range(0, cnto):
            print(B[i], end = ' ')
        print()
        # looping over count of even integers
        for i in range(0, cnte):
            print(C[i], end = ' ')
        print()
        T -= 1
    return 0

# if __name__ == '__main__':
#     main()