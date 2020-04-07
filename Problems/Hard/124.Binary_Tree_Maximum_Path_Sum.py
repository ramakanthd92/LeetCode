#Runtime - 80 ms   Memory - 26 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_path_sum = -float("inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs_helper(root):
            if not root:
                return 0
            l = dfs_helper(root.left)
            r = dfs_helper(root.right)
            
            self.max_path_sum  = max(self.max_path_sum , max(root.val + l + r, max(root.val + l ,root.val + r)))
            
            return max(max(l + root.val, r + root.val),0) 
    
        dfs_helper(root)
        return self.max_path_sum 
