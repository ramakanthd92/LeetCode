# Runtime - 20 ms   Memory -  12.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        dq = collections.deque()
        dq.append(root)
        
        l = 0
        empty = False
        while(len(dq) > 0):
            q_len = len(dq)
            empty = False
            for i in range(q_len):
                node = dq.popleft()
                #print node.val
                if node.left:
                    dq.append(node.left)
                    if empty:
                        return False
                else:
                    empty = True
                if node.right:
                    dq.append(node.right)
                    if empty:
                        return False
                else:
                    empty = True
            if len(dq) and q_len != pow(2,l):
                return False
            l += 1
        return True
