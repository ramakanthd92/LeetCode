class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        R,C= len(matrix),0
        if R:
            C = len(matrix[0])
        else:
            return 0
        
        max_square = [[0 for _ in range(C)] for _ in range(R)]
        
      
        for k in range(min(R,C)):
            for i in range(k,R):
                if k == 0:
                    if matrix[i][k] == "1":
                        max_square[i][k] = 1
                        
                else:
                    if matrix[i][k] == "1":
                        #print "a", i, k
                        max_square[i][k]  = min(max_square[i-1][k-1],min(max_square[i][k-1], max_square[i-1][k]))+1
                    else:
                        #print "b", i, k
                        max_square[i][k]  = 0
                    
            for j in range(k,C):
                if k == 0: 
                    if matrix[k][j] == "1":
                        max_square[k][j] = 1
                else:
                    if matrix[k][j] == "1":
                        #print "c" , k, j
                        max_square[k][j]  = min(max_square[k-1][j-1],min(max_square[k][j-1], max_square[k-1][j]))+1
                    else:
                        #print "d", k ,j
                        max_square[k][j] = 0
                        
        max_rect = 0
        
        for i in range(R):
            for j in range(C):
                max_rect = max(max_rect,max_square[i][j])
            
        return max_rect*max_rect
