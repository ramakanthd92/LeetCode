# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if not root:
            return
        self.stack.append(root)
        while (root.left):
            self.stack.append(root.left)
            root = root.left
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.stack:
            return None
        node = root =  self.stack.pop()
        if root.right:
            self.stack.append(root.right)
            root = root.right
            while (root.left):
                self.stack.append(root.left)
                root = root.left
        
        return node.val   
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.stack) > 0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
