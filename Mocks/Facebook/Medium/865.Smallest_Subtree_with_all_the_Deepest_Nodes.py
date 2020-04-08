# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_depth = 0
        self.deep_node = None
    
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return []
        
        def post_order_helper(root,level):
            if not root:
                return level
        
            left = post_order_helper(root.left,level+1)
            right = post_order_helper(root.right,level+1)
            
            if left == right and right >= self.max_depth:
                self.max_depth = left
                self.deep_node = root
            elif left > right and left > self.max_depth:
                self.max_depth = left
                self.deep_node = root.left                
            elif right > self.max_depth:
                self.max_depth = right
                self.deep_node = root.right
            
            return max(left,right)
        
        post_order_helper(root,0)
    
        return self.deep_node
                
                
