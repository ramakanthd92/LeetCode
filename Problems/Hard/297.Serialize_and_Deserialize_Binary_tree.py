# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Runtime - 136 ms    Memory - 23.1 MB

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []
        if not root:
            return res
        
        def bfs(root):
            dq = collections.deque()
            dq.append(root)
            res.append(root.val)
            while (len(dq) > 0):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append(None)
                if node.right:
                    dq.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append(None)
            
        bfs(root)
        
        N = len(res)
        i = N-1
        while(i > 0 and res[i] == None):
            i -= 1
            
        #print res[:i+1]
       # print res
        return res[:i+1]
                    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print len(data)
        #data_list = data[1:-1].split(",")
        def bfs_helper():
            par_qu = collections.deque()
            chi_qu = data[:]
            root_val = chi_qu.pop(0)
            node = TreeNode(root_val)
            par_qu.append([root_val,node])
            while(len(par_qu) > 0):
                left_ch, right_ch = None,None
                if len(chi_qu) > 0:
                    left_ch = chi_qu.pop(0)
                if len(chi_qu) > 0:
                    right_ch = chi_qu.pop(0)
                par_val,par_node = par_qu.popleft()
                if left_ch != None:
                    left_node = TreeNode(left_ch)
                    par_node.left = left_node
                    par_qu.append([left_ch,left_node])
                if right_ch != None:
                    right_node = TreeNode(right_ch)
                    par_node.right = right_node
                    par_qu.append([right_ch,right_node])              
            return node
            
        if len(data):
            return bfs_helper()
        return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
