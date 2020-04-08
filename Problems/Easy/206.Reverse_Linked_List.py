# Runtime - 28 ms   Memory - 13.9 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        curr = head
        pre = None
        while (curr.next):
            curr.next, pre, curr = pre,curr,curr.next
            
        curr.next, pre= pre,curr
        
        return curr
            
