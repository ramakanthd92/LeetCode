# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_diameter = 0
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        def helper(root):
            if not root:
                return 0
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            
            
            self.max_diameter = max(self.max_diameter, left_depth + right_depth )
            #print root.val, left_depth, right_depth, self.max_diameter 
            
            return max(left_depth,right_depth)+1
        
        
        helper(root)
        
        return self.max_diameter
    
