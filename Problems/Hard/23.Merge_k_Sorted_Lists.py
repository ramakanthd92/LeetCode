# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Runtime - 100ms    Memory - 17.9 MB

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k_list = []
        L = len(lists)
        lsp = [lists[i] for i in range(L)] 

        for i in range(L):
            if lsp[i]:
                k_list.append([lsp[i].val,lsp[i],i])
                tmp = lsp[i].next
                lsp[i].next = None
                lsp[i] = tmp

        heapq.heapify(k_list)
        
        res = None
        
        #print k_list
        
        head = tail = None
        while(len(k_list) > 0):
            node = heapq.heappop(k_list)
            #print node
            elem = node[1]
            index = node[2]
            #res.append(elem)
            #print elem, index
            if not head:
                head = tail = elem
            else:
                tail.next = elem
                tail = elem
            
            if lsp[index]:
                heapq.heappush(k_list,[lsp[index].val,lsp[index],index])
                tmp = lsp[index].next
                lsp[index].next = None
                lsp[index] = tmp
            
        return head
        
