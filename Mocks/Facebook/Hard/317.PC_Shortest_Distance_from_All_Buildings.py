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
        n = 3
        def bfs(i,j,n):
            dq = collections.deque()
            visited = set()
            dq.append((i,j))
            visited.add((i,j))
            count = 0
            level = 0
            tra_dist = 0
            while len(dq) > 0 and count < n:
                len_que = len(dq)
                for i in range(len_que):
                    r,c = dq.popleft()
                   # print r,c
                    for k,l in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if  0 <= r+k < R and 0 <= c+l < C:
                            if (r+k,c+l) not in visited:
                                if grid[r+k][c+l] == 0:
                                    dq.append((r+k,c+l))
                                if grid[r+k][c+l] == 1:
                                    count += 1
                                    tra_dist += level+1
                                  #  print r+k, c+l, count, tra_dist
                                visited.add((r+k,c+l))
                level += 1
            return tra_dist
        
        max_tra_dist = float("inf")
        for i in range(R):
            for j in range(C):
               # print i,j
                if grid[i][j] == 0:
                    max_tra_dist = min(bfs(i,j,n),max_tra_dist)
        if max_tra_dist == float("inf"):
            return -1
        return max_tra_dist
