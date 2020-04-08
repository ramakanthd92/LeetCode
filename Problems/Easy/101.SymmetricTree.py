# Runtime - 32 ms   Memory - 12.2 MB 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
            
        return self.isSymmetricHelper(root.left,root.right)
    
    def isSymmetricHelper(self, left, right):
        if  left == right == None:
            return True
        if not left or not right:
            return False
            
        left_ = self.isSymmetricHelper(left.left,right.right)
        right_ = self.isSymmetricHelper(left.right,right.left)
        
        return ((left.val == right.val) and left_ and right_)
        
        
