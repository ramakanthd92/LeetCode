# Runtime - 28 ms  Memory - 12.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = Queue()     
        q.put(root)
        tree = []
        while(q.qsize() > 0):
            q_size = q.qsize()
            level = []
            for _ in xrange(q_size):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            tree.append(level)
        return tree
            
