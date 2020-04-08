# Runtime - 20ms  Memory - 11.8 MB

import heapq
import collections

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        L = len(S)
        hash_map = collections.defaultdict()
        
        for i in range(L):
            if S[i] not in hash_map:
                hash_map[S[i]] = 1
            else:
                hash_map[S[i]] += 1
        lis = []
        for k,v in hash_map.items():
            heapq.heappush(lis,[-v,k]) 
            
        return self.output(lis,L)
    
    def output(self,lis,n):
        res = ""
        stk = []
        while len(res) < n:
            node = None
            while (len(res) > 0 and len(lis) > 0 and lis[0][1] == res[-1]):
                node = heapq.heappop(lis)
                if node:
                    stk.append(node)
                    
            if len(res) == 0:
                node = heapq.heappop(lis)
                if node:
                    stk.append(node)
            elif len(lis) > 0 and lis[0][1] != res[-1]:
                node = heapq.heappop(lis)
                if node:
                    stk.append(node)
            else:
                return ""
            
            res += node[1]
            node[0] += 1
                            
            while(len(stk) > 0):
                nd = stk.pop()
                if nd[0] < 0: 
                    heapq.heappush(lis,nd)            
            
        return res
