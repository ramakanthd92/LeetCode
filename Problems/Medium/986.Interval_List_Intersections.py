# Runtime - 136 ms   Memory - 12.4 MB

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return []
        
        i = 0
        j = 0
        st,en = 0,0
        res = []
        while(i < len(A) and j < len(B)):            
            st = max(A[i][0],B[j][0])
            en = min(A[i][1],B[j][1])
            if st <= en:
                res.append([st,en])
            
            if A[i][1] >= B[j][1]:
                j+= 1
            else:
                i+=1
                
        return res
            
    """
    [0,2][4,6][8,10]
    [1,5][6,6]
    
    i = 0, j = 0
    st = 0, en = 0
    
    res = [[1,2],
    
    
    """
