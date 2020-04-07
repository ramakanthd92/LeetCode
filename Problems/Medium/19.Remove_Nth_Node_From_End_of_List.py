# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Runtime - 28 ms    Memory - 12.9 MB  

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fp = head
        sp = head
        prev = None 
        
        def remove_node(prev,node):
            if prev:
                prev.next = node.next
            temp = node.next
            node.next = None
            node = temp
            return node
        
        i = 0
        while fp and i < n:
            fp = fp.next
            i+=1
            
        if i < n:
            return head
            
        while fp:
            fp = fp.next
            prev = sp
            sp = sp.next
            i+=1 
        
        if i == n:
            node = remove_node(prev,sp)
            return node
        
        remove_node(prev,sp)
        
        return head
