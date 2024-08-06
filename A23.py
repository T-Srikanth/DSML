# Intermediate DSA: Linked Lists - Basics
###################################################
######### Reference links #########
####################################################

## Design and implement a Linked List data structure. A "node" in a linked list should have the following attributes - an integer "value" and a "pointer" to the next node.
# It should support the following operations:
# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space (no trailing spaces).
# Note: If an input position does not satisfy the constraint, no action is required. Each print query has to be executed in a new line.
class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_node(self,position,data):
    new_node = Node(data)
    if position < 1: #Invalid position, do nothing      
      return
    if position == 1: #Insert at the head
      new_node.next = self.head
      self.head = new_node
      return
    #Traverse to the node just before the desired position
    current = self.head
    for _ in range(position-2):
      if current is None: #position is out of bounds, do nothing
        return
      current = current.next
    if current is None: #position is out of bounds, do nothing
      return
    #Insert the new node
    new_node.next = current.next
    current.next = new_node

  def delete_node(self,position):
    if position < 1: #Invalid position, do nothing
      return
    if position == 1:
      if self.head is not None: #Remove the head
        self.head = self.head.next
      return
    #Traverse to the node just before the desired position
    current = self.head
    for _ in range(position-2):
      if current is None: #Position is out of bounds, do nothing
        return
      current = current.next
    if current is None or current.next is None: #Position is out of bounds, do nothing
      return
    current.next = current.next.next

  def print_ll(self):
    current = self.head
    result = []
    while current is not None:
      result.append(str(current.data))
      current = current.next
    print(" ".join(result))
# ll = LinkedList()
# ll.insert_node(1,10)      
# ll.insert_node(2,20)
# ll.insert_node(3,30)
# ll.insert_node(4,40)
# ll.delete_node(2)
# ll.print_ll()

## Design Linked List 
# Given a matrix A of size Nx3 representing operations. Your task is to design the linked list based on these operations.
# There are four types of operations:
#   0 x -1: Add a node of value x before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#   1 x -1: Append a node of value x to the last element of the linked list.
#   2 x index: Add a node of value x before the indexth node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. 
#   If index is greater than the length, the node will not be inserted.
#   3 index -1: Delete the indexth node in the linked list, if the index is valid.
# A[i][0] represents the type of operation. A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.
# Note: Indexing is 0 based.
class Nodes:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedLists:
  def __init__(self):
    self.head = None

  def insert_nodes(self,data,position):
    new_node = Nodes(data)
    if position < 0:
      return False
    if position == 0:
      new_node.next = self.head
      self.head = new_node
      return True
    current = self.head
    for _ in range(position-1):
      if current is None:
        return False 
      current = current.next
    if current is None:
      return False
    new_node.next = current.next
    current.next = new_node
    return True
  
  def delete_nodes(self,position):
    if position < 0:
      return False
    if position == 0:
      if self.head is not None:
        self.head = self.head.next
        return True
      return False
    current = self.head
    for _ in range(position-1):
      if current is None:
        return False
      current = current.next
    if current is None or current.next is None:
      return False
    current.next = current.next.next
    return True

  def len_ll(self):
    current = self.head
    count = 0
    while current is not None:
      count += 1
      current=current.next
    return count

  def printer(self):
    current = self.head
    while current is not None:
      print(current.data, end='-->')
      current=current.next
    print('None')

def solve(A):
  rows=len(A)
  ll = LinkedLists()
  for i in range(rows):
    if A[i][0] == 0:
      ll.insert_nodes(A[i][1],0)
      ll.printer()
    elif A[i][0] == 1:
      pos = ll.len_ll()
      ll.insert_nodes(A[i][1],pos)
      ll.printer()
    elif A[i][0] == 2:
      ll.insert_nodes(A[i][1],A[i][2])
      ll.printer()
    elif A[i][0] == 3:
      ll.delete_nodes(A[i][1])
      ll.printer()
  return
# A = [[3,1,-1],[1,15,-1],[3,0,-1],[0,10,-1],[0,18,-1],[1,19,-1],[2,6,2],[0,11,-1]]
# solve(A)    

## Flatten Nested List Iterator
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
# NestedIterator(List nestedList) Initializes the iterator with the nested list nestedList. int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
class NestedIterator:
  def __init__(self, nestedList):
    self.actual = []
    self.idx = 0
    self._flatten(nestedList)
    self.n = len(self.actual)

  def _flatten(self, nestedList):
    for item in nestedList:
      if item.isInteger():
        self.actual.append(item.getInteger())
      else:
        self._flatten(item.getList())

  def next(self):
    self.idx += 1
    return self.actual[self.idx - 1]

  def hasNext(self):
    return self.idx < self.n

## Middle element of linked list
# Given a linked list of integers, find and return the middle element of the linked list.
# Note: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None
class Solution:
  # @param A : head node of linked list
  # @return an integer
  def solve(self, A):
    if not A or not A.next:
      return A
    # slow and fast pointer
    slow = fast = A
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    return slow.val
    
## Remove Duplicates from sorted list
# Given a sorted linked list, delete all duplicates such that each element appears only once.
def remove_duplicates(self,A):
  head = A
  while A:
    while A.next and A.next.val == A.val:
      A.next = A.next.next
    A = A.next
  return head