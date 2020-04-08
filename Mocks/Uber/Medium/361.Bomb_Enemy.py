class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r = len(grid)
        
        if not r:
            return 0
        
        c = len(grid[0])
        
        if not c:
            return 0
        
        
        
        def left_traverse_row(row):
            cnt = 0
            for i in range(c):
                if grid[row][i] == 'W':
                    cnt = 0
                elif grid[row][i] == 'E':
                    cnt += 1
                else:
                    grid[row][i] = int(grid[row][i]) + cnt
        
        def right_traverse_row(row):
            cnt = 0
            for i in range(c-1,-1,-1):
                if grid[row][i] == 'W':
                    cnt = 0
                elif grid[row][i] == 'E':
                    cnt += 1
                else:
                    grid[row][i] = int(grid[row][i]) + cnt
        
        def left_traverse_column(col):
            cnt = 0
            for i in range(r):
                if grid[i][col] == 'W':
                    cnt = 0
                elif grid[i][col] == 'E':
                    cnt += 1
                else:
                    grid[i][col] = int(grid[i][col]) + cnt
        
        def right_traverse_column(col):
            cnt = 0
            for i in range(r-1,-1,-1):
                if grid[i][col] == 'W':
                    cnt = 0
                elif grid[i][col] == 'E':
                    cnt += 1
                else:
                    grid[i][col] = int(grid[i][col]) + cnt
        
        # traverse all rows
        for j in range(r):
            left_traverse_row(j)
            right_traverse_row(j)
        
         # traverse all columns
        for j in range(c):
            left_traverse_column(j)
            right_traverse_column(j)
            
        #print grid
        
        max_enemies = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 'W' and  \
                    grid[i][j] != 'E':
                        max_enemies = max(max_enemies,grid[i][j])
                        
        return max_enemies
