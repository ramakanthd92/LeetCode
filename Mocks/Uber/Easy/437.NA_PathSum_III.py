# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path = [0 for _ in range(1000)]
        self.total_paths = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def helper(root, level):
            if not root:
                s =  check(level,sum)
                print s
                self.total_paths += s 
                return 0
            self.path[level] = root.val
            helper(root.left,level+1)   
            helper(root.right,level+1)   
            
        def check(level,sum):
            #print self.path
            #print level
            num_vals = 0
            sum_val = 0
            for i in range(level):
                j = i+1
                sum_val = 0
                while (j < level and sum_val < sum):
                    sum_val += self.path[i]
                    j += 1
                
                if sum_val == sum:
                    num_vals += 1
            return num_vals
        
        helper(root,0)
        return self.total_paths
