import collections

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        A_adj = collections.defaultdict() 
        B_adj = collections.defaultdict()
        
        AR = len(A)
        if not AR:
            return 0
        AC = len(A[0])
        
        BR = len(B)
        if not BR:
            return 0
        BC = len(B[0])
        
        for i in range(AR):
            dic = collections.defaultdict(int)
            for j in range(AC):
                if A[i][j]:
                    dic[j] = A[i][j]
            A_adj[i] = dic
        
        for i in range(BR):
            dic = collections.defaultdict(int)
            for j in range(BC):
                if B[i][j]:
                    dic[j] = B[i][j]
            B_adj[i] = dic
        
        
        res = [[0 for i in range(BC)] for j in range(AR)]
        
        for i in range(AR):
            if i in A_adj:   
                for k,v in A_adj[i].items():
                    if k in B_adj:
                        for j,l in B_adj[k].items():
                            res[i][j] += v*l
        
        return res
        
                
