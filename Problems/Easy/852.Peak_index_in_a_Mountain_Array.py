# Runtime - 68 ms   Memory - 13.7 MB

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = len(A) 
        if not L:
            return -1
        
        i = 0
        
        while(i-1 < L and A[i] < A[i+1]):
            i+=1
            
        return i
            
        
        
