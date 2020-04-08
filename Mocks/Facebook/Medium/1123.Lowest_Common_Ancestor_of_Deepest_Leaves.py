# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_depth = 0
        self.lca = None
        
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(root,level):
            if not root:
                return 0
            
            ld,rd = 0,0
            if root.left:
                ld = dfs(root.left,level+1)
            
            if root.right:
                rd = dfs(root.right,level+1)
            
            if max(ld,rd) + level > self.max_depth:
                self.max_depth = level + max(ld,rd)
            
            if ld == rd and  ld + level == self.max_depth:
                self.lca = root
                
            return max(ld,rd) + 1
       
        self.max_depth = 0
        self.lca = None
        
        dfs(root,0)
        
        return self.lca
