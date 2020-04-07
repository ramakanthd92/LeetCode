# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Runtime - 52 ms, Memory - 11.7 MB

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        res, ptr = None, None
        rem = 0
        while(l1 and l2):
            val = l1.val + l2.val + rem
            den = val%10
            node = ListNode(den)
            if not res:
                res = ptr = node
            else:
                ptr.next = node
                ptr = node
            rem = val/10
            l1 = l1.next
            l2 = l2.next
            
        l = None
        if l1:
            l = l1 
        else:
            l = l2
        
        while (l):
            den = (l.val + rem)%10
            node = ListNode(den)
            if not res:
                res = ptr = node
            else:
                ptr.next = node
                ptr = node
            rem = (l.val+rem)/10
            l = l.next
        
        if rem != 0:
            node = ListNode(rem)
            ptr.next = node
            ptr = node
        
        return res 
            
