# Runtime - 84 ms   Memory - 13.2 MB

import collections

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])
        
        n = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    n+=1
        
        hit, minDist = [[0] * C for i in range(R)], [[0] * C for i in range(R)]
    
        def bfs(i,j,n):
            dq = collections.deque()
            visited = set()
            dq.append((i,j))
            visited.add((i,j))
            count = 1
            level = 0
            tra_dist = 0
            while len(dq) > 0:
                len_que = len(dq)
                for i in range(len_que):
                    r,c = dq.popleft()
                   # print r,c
                    for k,l in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if  0 <= r+k < R and 0 <= c+l < C:
                            if (r+k,c+l) not in visited:
                                if grid[r+k][c+l] == 0:
                                    dq.append((r+k,c+l))
                                    hit[r+k][c+l] +=1
                                    minDist[r+k][c+l] += level+1
                                elif grid[r+k][c+l] == 1:
                                    count += 1
                                visited.add((r+k,c+l))
                level += 1
            return count == n
        
        max_tra_dist = float("inf")
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if not bfs(i,j,n):
                        return -1
        return min([minDist[i][j] for i in range(R) for j in range(C) if not grid[i][j] and hit[i][j] == n] or [-1])

                
        
        
                    

