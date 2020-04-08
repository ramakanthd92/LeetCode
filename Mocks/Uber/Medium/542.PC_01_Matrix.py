class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        if not r:
            return matrix
        c = len(matrix[0])
        if not c:
            return matrix
        
        visited = [[ 0 for _ in range(c)] for _ in range(r)] 
        output = [[ 10000 for _ in range(c)] for _ in range(r)] 
        
        def dfs(i,j,level):
            #print i,j,level
            if not ((0 <= i < r) and (0 <= j < c)):
                return 0
            #print matrix[i][j]
            if matrix[i][j] == 0:
                #output[i][j] = 0
                return 0
            elif output[i][j] < level:
                return 0
            
            elif output[i][j] > level and matrix[i][j] != -1:
                #print "->", i,j,level
                output[i][j]  = level
                
            visited[i][j] = 1
            for k,l in [(-1,0),(0,1),(1,0),(0,-1)]:
                if not ((0 <= i+k < r) and (0 <= j+l < c)):
                    continue
                if not visited[i+k][j+l]:
                    dfs(i+k,j+l,level+1)
            visited[i][j] = 0
            
        for i in range(r):
            for j in range(c):
                #print i,j
                if matrix[i][j] == 0:
                    visited = [[ 0 for _ in range(c)] for _ in range(r)] 
                    output[i][j] = 0       
                    matrix[i][j] = -1             
                    dfs(i,j,0)
                    matrix[i][j] = 0
                
                #print output
        return output
