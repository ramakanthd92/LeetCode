class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        N = len(A)
        if not N:
            return False
        
        i = 0
        while(i < N-1):
            if A[i] <= A[i+1]:
                i+=1
            else:
                break
                
        if i == N-1:
            return True
        
        i = 0
        while(i < N-1):
            if A[i] >= A[i+1]:
                i+=1
            else:
                break
                
        if i == N-1:
            return True
        
        return False
