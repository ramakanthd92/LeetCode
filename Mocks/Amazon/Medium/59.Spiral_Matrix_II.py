class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        N = n*n
        
        
        """
         0,0 -> 0,N-2
         0,N-1 -> N-2,N-1
         N-1,N-1 -> N-1,1
         N-1,0 -> 1,0
        
         0,0 ->

         1,1 -> 1,N-3
         1,N-2 -> N-3,N-2
         N-2,N-2 -> N-2, 2
         N-2,1 -> 2,1
         
        """
        if n ==0:
            return []
        
        A = [[0 for _ in range(n)] for _ in range(n)]
        
        a = 1
        for l in range(0,(n//2)):
            #print l
            i = l
            for j in range(l,n-1-l):
                #print i,j
                A[i][j] = a
                a += 1
            j = n-1-l
            for i in range(l,n-1-l):
                #print i,j
                A[i][j] = a
                a += 1
            i = n-1-l
            for j in range(n-1-l,l,-1):
                #print i,j
                A[i][j] = a
                a += 1            
            j = l
            for i in range(n-1-l,l,-1):
                #print i,j
                A[i][j] = a
                a += 1
           
        if n%2 != 0:
            A[n//2][n//2] = n*n 
        
        return A
