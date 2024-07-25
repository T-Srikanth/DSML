# Intermediate DSA: Strings
###################################################
######### Reference links #########
####################################################

## Reverse the string
# You are given a string A of size N. Return the string A after reversing the string word by word.
# Note: A sequence of non-space characters constitutes a word.
#       Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
#       If there are multiple spaces between words, reduce them to a single space in the reversed string.
def reverse_words(S):
  s_list = S.split(" ")
  n= len(s_list)
  i,j=0,n-1
  while i<j:
    s_list[i],s_list[j]=s_list[j],s_list[i]
    i += 1
    j -= 1
  return " ".join(s_list)
# S ="the sky is blue"
# print(reverse_words(S))
#OR
def solve(A):
  A = A.strip()
  A = A.split()
  A = A[::-1]
  return ' '.join(A)

## Simple Reverse
# Given a string A, you are asked to reverse the string and return the reversed string.
def reverse_char(S):
  s_list = list(S)
  s_list = s_list[::-1]
  return "".join(s_list)
# A = "scaler"
# print(reverse_char(A))
#OR
def solve(A):
  n = len(A)
  ans = ""
  for i in range(n-1, -1, -1):
    ans += A[i]
  return ans

## toLower()
# You are given a function to_lower() which takes a character array A as an argument. Convert each character of A into lowercase characters if it exists. If the lowercase of a character does not exist,
# it remains unmodified.The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.Return the lowercase version of the given character array.
def toLower(A):
  n = len(A)
  for i in range(n):
    if 65<=ord(A[i])<=90:
      A[i]=chr(ord(A[i])^32)
  return A
# A = ['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']
# print(toLower(A))
#OR
def to_lower(A):
  s = ''
  for c in A:
    if c >= 'A' and c <= 'Z':
      s = s + chr((ord(c) + 32))
    else:
      s = s + c
  return s

## toUpper()
# You are given a function to_upper() consisting of a character array A. Convert each character of A into Uppercase character if it exists. If the Uppercase of a character does not exist, 
# it remains unmodified.The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.Return the uppercase version of the given character array.
def toUpper(A):
  n= len(A)
  for i in range(n):
    if 97<=ord(A[i])<=122:
      A[i] = chr(ord(A[i])^32)
  return A
# A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']
# print(toUpper(A))
#OR
def to_upper(self, A):
  s = ''
  for c in A:
    if c >= 'a' and c <= 'z':
      s = s + chr((ord(c) - 32))
    else:
      s = s + c
  return s

## isalnum()
# You are given a function isalnum() consisting of a character array A. Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.
def isalnum(A):
  for c in A:
    if ('a'<=c<='z') or ('A'<=c<='Z') or ('0'<=c<='9'):
      continue
    else:
      return 0
  return 1
# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
# print(isalnum(A))

## isalpha()
# You are given a function isalpha() consisting of a character array A. Return 1 if all the characters of a character array are alphabetical (a-z and A-Z) else, return 0.
def isalpha(A):
  for c in A:
    if ('a'<=c<='z') or ('A'<=c<='Z'):
      continue
    else:
      return 0
  return 1
# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']
# print(isalpha(A))
#OR
def solve_alpha(A):
  for x in A:
    if(x.isalpha() == 0):
      return 0
  return 1

## Longest Palindromic Substring
# Given a string A of size N, find and return the longest palindromic substring in A. Substring of string A is A[i...j] where 0 <= i <= j < len(A)
# Palindrome string: A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
# Incase of conflict, return the substring which occurs first ( with the least starting index).
def long_palindrome(A):
  a_list = list(A)
  n = len(a_list)
  ans = 1
  s = ''
  for i in range(n):  #loop for odd length palindrome
    j,k=i-1,i+1
    p_len=1
    while j>=0 and k<n:
      if A[j]==A[k]:
        p_len += 2
      j -= 1
      k += 1
    if p_len>ans:
      ans = max(ans, p_len)
      s = A[i-ans//2:i+ans//2+1]

  for i in range(n-1):  #loop for even length palindrome
    j=i+1
    x,y= i-1, j+1
    if A[i]!=A[j]:
      continue
    else:
      p_len=2
      while x>=0 and y<n:
        if A[x]==A[y]:
          p_len += 2
        x -= 1
        y += 1
      if p_len>ans:
        ans = max(ans, p_len)
        s = A[i-(ans-2)//2:j+(ans-2)//2+1]
  return s
# A = "aaaabaaaa"
# print(long_palindrome(A))
#OR
def longestPalindrome(A):
  aLen = len(A)
  if aLen == 0:
    return A
  A2 = "|"
  for x in A:
    A2 += x + "|"
  p = [0] * (2 * aLen + 1)
  c = 0
  r = 0
  m = 0
  n = 0
  for i in range(1, 2 * aLen + 1):
    if i > r:
      p[i] = 0
      m = i - 1
      n = i + 1
    else:
      i2 = c * 2 - i
      if p[i2] < r - i:
        p[i] = p[i2]
        m = -1
      else:
        p[i] = r - i
        n = r + 1
        m = i * 2 - n
    while m >= 0 and n < 2 * aLen + 1 and A2[m] == A2[n]:
      p[i] += 1
      m -= 1
      n += 1
    if i + p[i] > r:
      c = i
      r = i + p[i]
  leng = 0
  c = 0
  for i in range(1, 2 * aLen + 1):
    if leng < p[i]:
      leng = p[i]
      c = i
  ret = A2[c - leng + 1 : c + leng + 1 : 2]
  return ret
A = "aaaabaaaa"
print(longestPalindrome(A))

## Toggle Case
# You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
# You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.
def toggle_case(A):
  n=len(A)
  a_list=list(A)
  for i in range(n):
    a_list[i]=chr(ord(a_list[i])^32)
  return ''.join(a_list)
# A='tHiSiSaStRiNg'
# print(toggle_case(A))

## Is it Palindrome?
# You have a string (A) and you have to return 1 if it is palindrome otherwise return 0.
def is_palindrome(A):
  n=len(A)
  i,j=0,n-1
  while i<j:
    if A[i]!=A[j]:
      return 0
    i += 1
    j -= 1
  return 1
# A = "abba"
# print(is_palindrome(A))
#OR
def solve(A):
  for i in range(0,len(A)):
    if A[i] != A[len(A)-i-1]:
      return 0
  return 1

## Amazing Subarrays
# You are given a string S, and you have to find all the amazing substrings of S. An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
def ama_substrings(S):
  n = len(S)
  se = set(['a','e','i','o','u','A','E','I','O','U'])
  count = 0
  for i in range(n-1, -1, -1):
    if S[i] in se:
      count += n-i
  return count
# S = 'ABEC'
# print(ama_substrings(S))

## Count Occurrences
# Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
def count_bob(A):
  s='bob'
  n=len(A)
  count =0
  for i in range(n-len(s)+1):
    if A[i:i+len(s)]==s:
      count += 1
  return count
# A = 'bobob'
# print(count_bob(A))
#OR
def solve(A):
  s = A
  prev = -1
  ans = 0
  cur = s.find("bob", prev+1)
  while cur != -1:
    ans += 1
    prev = cur
    cur = s.find("bob", prev+1)
  return ans

## Change character
# You are given a string A of size N consisting of lowercase alphabets. You can change at most B characters in the given string to any other lowercase alphabet such that the number
# of distinct characters in the string is minimized. Find the minimum number of distinct characters in the resulting string.
def change_char(A,B):
  n = len(A)
  freq = [0]*26
  distinct_char = 0
  d_list_freq =[]
  for i in range(n):
    freq[ord(A[i])-97] += 1
  freq.sort()
  for cnt in freq:
    if cnt>0:
      d_list_freq.append(cnt)
      distinct_char += 1
  for i in range(len(d_list_freq)):        
    if d_list_freq[i]>B:
      return distinct_char
    else:
      B -= d_list_freq[i]
      distinct_char -=1
  return distinct_char
# A = "abcabbccd"
# B = 3
# print(change_char(A,B))
#OR
def solve(self, A, B):
  n = len(A)
  arr = [0]*26
  ans = 0
  for i in A:
    arr[ord(i)-97] += 1
    if(arr[ord(i)-97] == 1):
      ans += 1
  arr.sort()
  for i in range(26):
    if(B-arr[i] >= 0 and arr[i] != 0):
      ans -= 1
      B -= arr[i]
  ans = max(ans, 1)
  return ans
 
## String operations
# Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
#        Concatenate the string with itself.
#        Delete all the uppercase letters.
#        Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
# Note: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
def str_operations(A):
  A += A
  n=len(A)
  vowels = ['a','e','i','o','u']
  ans = ''
  for char in A:
    if 'a'<=char<='z':
      if char in vowels:
        ans += '#'
      else:
        ans += char
  return ans
# A="AbcaZeoB"
# print(str_operations(A))

## Longest Common Prefix
# Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array. The longest common prefix for a pair of strings S1 and S2 is the 
# longest string S which is the prefix of both S1 and S2.
# Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
def long_common_prefix(A):
  n=len(A)
  min_str=A[0]
  ans = ''
  for i in range(1,n):
    if len(A[i])<len(min_str):
      min_str=A[i]
  flag = 0
  for i in range(len(min_str)):
    for j in range(n):
      if A[j][i] != min_str[i]:
        flag = 1
        break
    if flag != 1:
      ans += min_str[i]
  return ans
# A = ["abcdefgh", "abfghijk", "abcefgh"]
# print(long_common_prefix(A))
#OR
def longestCommonPrefix(self, A):
  n = len(A)
  if n < 1:
    return ""
  prefix = A[0]
  prefixLen = len(prefix)
  for i in range(1, n):
    j = 0
    while j < min(prefixLen, len(A[i])):
      if prefix[j] != A[i][j]:
        break
      j += 1
    if j < prefixLen:
      prefix = prefix[:j]
      prefixLen = j
  return prefix
