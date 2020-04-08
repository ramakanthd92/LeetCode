# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print self.reverseNumber(l1)
        print self.reverseNumber(l2)
        
        
            
    def reverseNumber(self,l1):
        l3 = None
        while (l1):
            l2 = l1.next
            l1.next = l3
            l3 = l1
            l1 = l2
    
        return l3
