# Runtime - 24 ms   Memory -11.9 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        new_list = None
        list1 = l1
        list2 = l2
        
        while (list1 and list2):
            if not head:
                if list1.val < list2.val:
                    head = new_list = list1
                    list1 = list1.next
                    head.next = None
                else:
                    head = new_list = list2
                    list2 = list2.next
                    head.next = None
            else:
                if list1.val < list2.val:
                    new_list.next = list1
                    list1 = list1.next
                    new_list = new_list.next
                else:
                    new_list.next = list2
                    list2 = list2.next
                    new_list = new_list.next
       
        if list1:
            if new_list: 
                new_list.next = list1
                list1 = list1.next
                new_list = new_list.next
            else:
                return list1
        
        if list2:
            if new_list:
                new_list.next = list2
                list2 = list2.next
                new_list = new_list.next
            else:
                return list2
            
        return head
