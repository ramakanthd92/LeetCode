# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        dq = collections.deque()
        dq.append(root)
        
        res = []
        
        while (len(dq) > 0):
            q_len = len(dq)
            for i in range(q_len):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                
            res.append(node.val)
        
        return res
            
