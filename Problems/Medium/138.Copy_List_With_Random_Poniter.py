# Runtime - 44 ms Memory - 12.6 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        
        slow = head
        # creating new nodes
        while slow:
            temp = slow.next
            new_node = Node(slow.val,temp,None)
            slow.next = new_node
            slow = temp
        
        slow = head
        fast = head.next
        
        # Assigning random pointers
        while slow:
            if slow.random:
                fast.random = slow.random.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
            slow = slow.next.next
        
        # seperating nodes into seperate lists
        new_copy = None
        new_copy = head.next
        slow = head
        fast = head.next
        
        while fast:     
            fast_temp = None
            slow_temp = slow.next.next
            if fast.next:
                fast_temp = fast.next.next                
            slow.next = slow_temp
            fast.next = fast_temp
            
            fast = fast_temp
            slow = slow_temp
       
        return new_copy
    
