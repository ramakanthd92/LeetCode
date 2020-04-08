# Runtime - 780 ms  Memory - 15.2 MB

import heapq
import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        L = len(tasks)
        hash_map = collections.defaultdict()
        
        for i in range(L):
            if tasks[i] not in hash_map:
                hash_map[tasks[i]] = 1
            else:
                hash_map[tasks[i]] += 1
                
        lis = []          
        for k,v in hash_map.items():
            heapq.heappush(lis,[-v,k])
        
        stk = []
        
        node = heapq.heappop()
    
        res = []
        res.append(node[1])
        node[0] += 1
        
        stk.append(node)
        
        while(len(lis) > 0 and len(stk) > 0):
        
            node = heapq.heappop()
            if len(res) > n:
                last_n =  res[-n-1:-1]
            else:
                last_n = res  
                
            if node[1] not in last_n:
                res.append(node[1])
                node[0] += 1
        
            
            stk.append(node)
        
        
        
        
        
        
        
