# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxint as MAXVAL 

class Solution(object):
    def __init__(self):
        self.min_depth = MAXVAL
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def dfs_helper(root, level):
            if not root:
                return level
            
            left, right = 0,0
            if root.left:
                left = dfs_helper(root.left, level+1)
            
            if root.right:
                right = dfs_helper(root.right, level+1)
                
            if not root.left and not root.right:
                if level < self.min_depth:
                    self.min_depth = level
                return level
            
            return max(left,right)
            
        dfs_helper(root, 0)
        
        return self.min_depth + 1
