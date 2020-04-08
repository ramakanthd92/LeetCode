# Runtime - 748 ms   Memory - 30.8 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        
        def recurse(node,path):
            if not node:
                #ans.append(0)
                return 0
            ret = recurse(node.next,path)
            while(len(path) > 0 and path[-1].val <= node.val):
                path.pop()
            if len(path) == 0:
                ans.append(0)
            else:
                ans.append(path[-1].val)
            path.append(node)
           
        path = []
        ans = []
        recurse(head,path)
        return ans[::-1]
