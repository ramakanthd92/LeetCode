# Runtime - 160 ms     Memory - 20.7 MB

class Solution(object):
    def __init__(self):
        self.visited = None
        self.grid_set = set()
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        xlen = len(grid)
        ylen = len(grid[0])
        self.visited = [[0 for i in range(ylen)] for j in range(xlen)] 
                
        for i in xrange(xlen):
            for j in xrange(ylen):
                if grid[i][j] == '1':
                    self.grid_set.add((i,j))
                    
        island_count = 0
        while len(self.grid_set) > 0:
            island_count += 1
            (r,c) = self.grid_set.pop()
            self.dfs(grid,r,c,xlen,ylen)
        return island_count
        
    def dfs(self,grid,i,j,xlen,ylen):
        if  (i < 0 or i >= xlen) or (j < 0 or j >= ylen):
            return
        self.visited[i][j] = 1
        if grid[i][j] == '1':
            if (i,j) in self.grid_set:
                self.grid_set.remove((i,j))
            
        for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if  (i+x >= 0 and i+x < xlen) and (j+y >= 0 and j+y < ylen):
                if not self.visited[i+x][j+y] and grid[i+x][y+j] == '1':
                    self.dfs(grid,i+x,j+y,xlen,ylen)
                
