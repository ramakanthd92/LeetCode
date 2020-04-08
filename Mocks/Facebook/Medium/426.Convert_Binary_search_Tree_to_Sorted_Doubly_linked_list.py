"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def __init__(self):
        self.last = None
        self.first = None
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        def helper(root):
            if not root:
                return None
            helper(root.left)
            if self.last:
                root.left = self.last 
                self.last.right = root
            else:
                self.first = root
            self.last = root
            
            helper(root.right)
        
        
        if not root:
            return root
        
        helper(root)
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first
                
