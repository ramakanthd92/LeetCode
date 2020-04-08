# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if L > R:
            return 0
        if not root:
            return 0
        
        def helper(root,L,R):
            if not root:
                return 0
            #print root.val
            if root.val < L:
                return helper(root.right,L,R)
            elif root.val > R:
                 return helper(root.left,L,R)
            else:
                 return helper(root.left,L,R) + \
                        helper(root.right,L,R) +\
                        root.val
                
        return helper(root,L,R)
