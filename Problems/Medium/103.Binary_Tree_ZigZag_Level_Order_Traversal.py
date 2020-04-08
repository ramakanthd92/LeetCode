# Runtime - 16 ms    Memory - 12.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()     
        q.append(root)
        tree = []
        level = 0
        while(len(q) > 0):
            q_size = len(q)
            levels = []
            for _ in xrange(q_size):
                node = q.popleft()
                levels.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if (level % 2):
                tree.append(reversed(levels))
            else:
                tree.append(levels)
            level += 1
        return tree
        
