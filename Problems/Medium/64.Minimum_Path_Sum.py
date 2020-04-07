# Runtime - 96 ms    Memory - 15.1 MB

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        
        grid_sum = [[float("inf") for i in range(n)] for j in range(m)]
        
        for gap in range(m+n):
            for j in range(0,gap):
                i = gap-j-1
                #print i,j
                if i == 0 and j == 0:
                    grid_sum[i][j] = grid[i][j]     
                    continue
                    
                if i>= m or j >= n:
                    continue
                    
                if i > 0 and j > 0:  
                    grid_sum[i][j] = min(grid_sum[i-1][j], grid_sum[i][j-1]) + grid[i][j]
                elif i == 0:
                    grid_sum[i][j] = grid_sum[i][j-1] + grid[i][j]
                elif j == 0:
                    #print i,j
                    grid_sum[i][j] =  grid_sum[i-1][j] + grid[i][j]
                
        return grid_sum[m-1][n-1]
