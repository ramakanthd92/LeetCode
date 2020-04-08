# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        
        dq = collections.deque()
        level = 1
        dq.append(root)
        
        max_sum, maximal_level= 0,0
        
        while (len(dq) > 0):
            level_sum = 0
            len_level  = len(dq)
            for i in range(len_level):
                node = dq.popleft()
                level_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                    
            if max_sum < level_sum:
                max_sum = level_sum
                maximal_level = level
                
            level += 1
            
        return maximal_level
