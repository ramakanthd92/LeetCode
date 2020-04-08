# Runtime - 32 ms    Memory - 14.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sys import maxint as MAXVAL

MAX_VAL = MAXVAL
MIN_VAL = -MAXVAL-1

class Solution(object):
    def __init__(self):
        self.max_diameter = MIN_VAL
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root):
            if not root:
                if self.max_diameter < 0:
                    self.max_diameter = 0
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            if self.max_diameter <  left + right + 1:
                self.max_diameter = left + right + 1
            
            return max(left,right) + 1 
            
        helper(root)
        return max(0,self.max_diameter-1)
            
