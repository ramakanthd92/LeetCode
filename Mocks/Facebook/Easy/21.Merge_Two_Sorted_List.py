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
        
        ptr1 = l1
        ptr2 = l2
        
        output = None
        output_ptr = None
        
#         A -> B 
        
#         X -> A 
        
        def remove_node(ptr, output):
            if ptr == None:
                return output,ptr
            if output:
                output.next = ptr
            output = ptr
            temp = ptr.next
            ptr.next = None
            ptr = temp
            #print output.val,ptr.val
            return output,ptr
        
        while ptr1 and ptr2:
            print ptr1.val, ptr2.val
            if ptr1.val <= ptr2.val:
                if not output:
                    output,ptr1 = remove_node(ptr1,output)
                    output_ptr = output
                else:
                    output_ptr ,ptr1 = remove_node(ptr1,output_ptr)
               # ptr1 = ptr1.next
            else:
                if not output:
                    output,ptr2 = remove_node(ptr2,output)
                    output_ptr = output
                else:
                    output_ptr, ptr2 = remove_node(ptr2,output_ptr)
               # ptr2 = ptr2.next
            
        if ptr1 and output_ptr:
            output_ptr.next = ptr1
        elif ptr1:
            output = ptr1
            
        if ptr2 and output_ptr:
            output_ptr.next = ptr2
        elif ptr2:
            output = ptr2
            
        return output
