# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sys import maxint as MAXVAL

MINVAL = -MAXVAL-1

class Solution(object):
    def __init__(self):
        self.close_max = MAXVAL
        self.close_min = MINVAL
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        
        r = self.searchClosest(root,target)
    
        if r:
            return root.val
        
        if self.close_max == MAXVAL and self.close_min == MINVAL:
            return None
        
        if self.close_max == MAXVAL:
            return self.close_min
        
        if self.close_min == MINVAL:
            return self.close_max
        
        if self.close_max - target < target - self.close_min:
            return self.close_max
        else:
            return self.close_min
    
    """
        4 
        
      2   5
      
    1  3 
    
    cmx = MAX
    cmn = MIN
    
    t = 3.714
    
    cmx = 4
    cmn = 2
    
    cmn = 3
    """
    

    def searchClosest(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        if root.val > target:
            self.close_max = min(self.close_max, root.val)
            self.searchClosest(root.left,target)
        elif root.val < target:
            self.close_min = max(self.close_min, root.val)
            self.searchClosest(root.right,target)
        else:           
            self.close_min = max(self.close_min, root.val)
            return root
        
