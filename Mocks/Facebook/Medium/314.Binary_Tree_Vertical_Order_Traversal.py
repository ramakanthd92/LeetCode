# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        hash_map = defaultdict()
        
        if not root:
            return []
        
        def dfs(root,row,col):
            if not root:
                return
            if col not in hash_map:
                hash_map[col] = defaultdict(list)
            hash_map[col][row].append(root.val)
            
            dfs(root.left,row+1,col-1)
            dfs(root.right,row+1,col+1)
        
        dfs(root,0,0)
        res = []
        for k in sorted(hash_map.keys()):
            row_res = []
            for v in sorted(hash_map[k].keys()):
                row_res += hash_map[k][v]
            res.append(row_res)
            
        return res
