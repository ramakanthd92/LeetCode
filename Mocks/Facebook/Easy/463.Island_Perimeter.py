import collections

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R,C = len(grid),0
        if not R:
            return 0
        C = len(grid[0])
        
        def bfs(i,j):
            dq = collections.deque()
            dq.append((i,j))
            visited = set()
            visited.add((i,j))
            perimeter = 0
            while(len(dq) > 0):
                
                r,c = dq.popleft()
                
                for k,l in [(-1,0),(0,1),(1,0),(0,-1)]:
                    if  0 <= r+k < R and 0 <= c+l < C:
                        if (r+k,c+l) not in visited:
                            if grid[r+k][c+l]:
                                dq.append((r+k,c+l))
                                visited.add((r+k,c+l))
                            else:
                                perimeter += 1                      
                    else:
                        perimeter += 1
                        
            return perimeter
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    return bfs(i,j)
                
        return 0
