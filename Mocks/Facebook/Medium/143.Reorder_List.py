# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return head 
        
        def cut_list(l1):
            fast, slow = l1,l1
            prev = None
            while(slow and fast):
                prev = slow
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            
            prev.next = None    
            return l1,slow
       
        def reverse_list(l1):
            slow = l1
            rev_head = None
            while slow:
                temp = slow.next    
                if not rev_head:
                    rev_head = slow
                    slow.next = None
                else:
                    slow.next = rev_head
                    rev_head = slow                      
                slow = temp 
                
            return rev_head
       
        def merge_list_wrap(l1,l2):
            head, tail = None, None
            while(l1 and l2):
                tl1 = l1.next
                tl2 = l2.next
                if not head:
                    head = tail = l1
                    l1.next = l2
                    l2.next = None
                    tail = l2
                else:
                    tail.next = l1
                    l1.next = l2
                    l2.next = None
                    tail = l2
                    
                l1 = tl1
                l2 = tl2                
                #print l1,l2,head
                
            if l1 and tail: 
                tail.next = l1
            elif l2 and tail:
                tail.next = l2
            return head
                
        front, back = cut_list(head)
        #print front, back
        rev_back = reverse_list(back)
        #print rev_back
        merge_list = merge_list_wrap(front,rev_back)
        
        return merge_list
                
