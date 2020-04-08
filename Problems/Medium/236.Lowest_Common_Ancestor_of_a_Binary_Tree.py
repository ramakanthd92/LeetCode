# Runtime - 72 ms  Memory - 24.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lca_found = False
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        lca = self.lcaHelper(root,p,q)
        if self.lca_found:
            return lca
        return None
        
    def lcaHelper(self, root, p, q):
        if not root:
            return None
        
        left = self.lcaHelper(root.left,p,q)
        right = self.lcaHelper(root.right,p,q)
        
       # print root,left,right
        
        if root == p or root == q:
            #print root
            if(left or right):
                self.lca_found = True
                return root
            else:
                return root
        
        if left and right:
            self.lca_found = True
            return root
        if left:
            return left
        if right:
            return right
        return None
