"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""

"""
UNDERSTAND: 


PLAN:
is root.left.value < root.value ?
is root.right.value > root.value ?
is root.left valid ?
is root.right valid ?

need to make sure the child nodes are within the allowed bounds of their position in the tree 
in comparison to the root 

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_height(root):
    if root is None:
        return 0
    else:
        return 1 + max(get_height(root.left), get_height(root.right))

def balancedBinaryTree(root):
    if root is None:
        return True
    
    return balancedBinaryTree(root.right) and balancedBinaryTree(root.left) and abs(get_height(root.left) - get_height(root.right)) <= 1
    # return balancedBinaryTree(root.right) 
    # and balancedBinaryTree(root.left) 
    # and abs(get_height(root.left) - get_height(root.right)) <= 1

#  revised solution 
"""
REVISED: 
new helper function will return the height of the tree if balanced, oterwise will return -1 
- apply the helper function to both sides of the tree root 
- if either side of the tree is unbalanced then we return -1 
- if both sub trees return an int value (the height of the sides), then we will check the difference in these heights 
    - if this difference does not exceed 1, then we will return the height of the tree 
    - if this difference does exceed 1, then we will return -1 

"""
def is_balanced_helper(root):
    if root is None:
        return 0
    
    left_height = is_balanced_helper(root.left)
    if left_height == -1:
        return -1
    
    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1
    
    if abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1

def balancedBinaryTree(root):
    return is_balanced_helper(root) > -1