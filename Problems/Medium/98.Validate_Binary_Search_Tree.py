# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Runtime - 36 ms  Memory - 16.8 MB

class Solution(object):
    def __init__(self):
        self.isValid = True
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lmin,rmax = self.isValidBSTHelper(root)
        
        return self.isValid
        
        
    def isValidBSTHelper(self,root):
        if not root:
            return None, None
        lmin,lmax = self.isValidBSTHelper(root.left)
        rmin,rmax = self.isValidBSTHelper(root.right)
        
        root_min, root_max = None,None
        
        if lmax and lmax >= root.val:     
            self.isValid = False
        if rmin and rmin <= root.val:
            self.isValid = False
        
        if lmin:
            root_min = min(lmin,root.val)
        else:
            root_min = root.val
        if rmax:
            root_max = max(rmax, root.val)
        else:
            root_max = root.val
        
        return root_min, root_max
    
