# Runtime - 440 ms    Memory - 12.5 MB

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        R,C = len(matrix),0
        if R:
            C  = len(matrix[0])
            
        len_matrix = [[0 for j in range(C)] for i in range(R)]
        visited = [[False for j in range(C)] for i in range(R)]
        
        
        def dfs_helper(i,j):
            if not(0 <= i < R and 0 <= j < C):
                return 0
            
            if len_matrix[i][j] > 0:
                return len_matrix[i][j]
            
            lr,rr,br,ur = 0,0,0,0
            if 0 <= i+1 < R and matrix[i][j] < matrix[i+1][j]:
                len_matrix[i][j] = max(len_matrix[i][j],dfs_helper(i+1,j))
            if 0 <= i-1 < R and matrix[i][j] < matrix[i-1][j]:
                len_matrix[i][j] = max(len_matrix[i][j],dfs_helper(i-1,j))
            if 0 <= j+1 < C and matrix[i][j] < matrix[i][j+1]:
                len_matrix[i][j] = max(len_matrix[i][j],dfs_helper(i,j+1))
            if 0 <= j-1 < C and matrix[i][j] < matrix[i][j-1]:
                len_matrix[i][j] = max(len_matrix[i][j],dfs_helper(i,j-1))
                
            len_matrix[i][j]+=1
                        
            return len_matrix[i][j]
        
        ans = 0
        for i in range(R):
            for j in range(C):
                ans =  max(ans,dfs_helper(i,j))
            
        return ans
