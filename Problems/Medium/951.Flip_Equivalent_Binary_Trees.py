# Runtime - 20 ms    Memory - 12.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def helper(root1,root2):
            if root1 == root2 == None:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1.val != root2.val:
                return False
            return ((helper(root1.left,root2.left) and helper(root1.right,root2.right)) or  
                        (helper(root1.left,root2.right) and helper(root1.right,root2.left)))            
        return helper(root1,root2)
