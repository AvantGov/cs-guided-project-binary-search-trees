"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""

"""
UNDERSTAND: 
we want to rach the longest point in which an item is a leaf node, where there are no children 
if the root it leaf, then the max depth is 1 
if we are given a different node to look at, then we are going to return a different value 
    since we can consider any node in the tree the "root"



PLAN: 
base case: if root is None, return 0
base case: if there is no left or right, then return 1 

if we have a left or right child:
    - get max depth of left child 
    - get max depth of right child
    - add 1 to the greater of the two max depths 

return the result 

"""



class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    # base case: if root is None, return 0
    if root is None:
        return 0
    
    # base case: if there is no left or right, return 1 
    if root.left is None and root.right is None:
        return 1
    
    # getting max depth of left node
    left_depth =  maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # compare the two and add 1 
    max_depth = 1 + max(left_depth, right_depth)

    return max_depth
