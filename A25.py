# Intermediate DSA: Trees Basics - 1
###################################################
######### Reference links #########
####################################################

## Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
class Solution:
	# @param A : root node of tree
	# @return a list of integers
  def inorderTraversal(self, A):
    def inorder(node):
      if node is None:
        return []
      # Traverse the left subtree, then current node, then right subtree
      return inorder(node.left) + [node.val] + inorder(node.right)
    return inorder(A)
## Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes values.
  def preorderTraversal(self,A):
    def preorder(node):
        if node is None:
          return []
        return [node.val] + preorder(node.left) + preorder(node.right)
    return preorder(A)
## Postorder Traversal
# Given a binary tree, return the Postorder traversal of its nodes values.
  def postorderTraversal(self,A):
    def postorder(node):
      if node is None:
        return []
      return postorder(node.left) + postorder(node.right) + [node.val]
    return postorder(A)

## Tree Height
# You are given the root node of a binary tree A. You have to find the height of the given tree. 
# A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.
  def treeHeight(self,A):
    def height(node):
      if node is None:
        return 0
      return 1 + max(height(node.left),height(node.right))
    return height(A)

## Identical Binary Trees
# Given two binary trees, check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
def isSameTree(A,B): #where A and B are root nodes of two trees
  def checkSame(x,y):
    if x is None and y is None:
      return 1
    if x is None or y is None:
      return 0
    return 1 if ((x.val==y.val) and checkSame(x.left,y.left) and checkSame(x.right,y.right)) else 0
  return checkSame(A,B)
    
## Counting the nodes
# Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestors.
# Ancestor means that every node that occurs before the current node in the path from root to the node.
def countMaxNodes(A):
  def count(root,maxVal):
    if root is None:
      return 0
    ans = 0
    if root.val > maxVal:
      ans = 1
    maxVal = max(maxVal,root.val)
    ans += count(root.left,maxVal)
    ans += count(root.right,maxVal)
    return ans
  return count(A,0)

## Nodes count
# You are given the root node of a binary tree A. You have to find the number of nodes in this tree.
def nodeCount(A):
  if A == None:
    return 0
  return 1 + nodeCount(A.left) + nodeCount(A.right)