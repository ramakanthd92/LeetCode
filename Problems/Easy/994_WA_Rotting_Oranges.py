# Runtime -   Memory -

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        q = collections.deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    cnt += 1
                if grid[i][j] == 2:
                    q.append((i, j))
            timer  = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    #print m,n
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        cnt -= 1
                        q.append((new_x, new_y))
            timer += 1
        return timer-1

# if __name__ == '__main__':
#   arr = [[0,1,2],
#         [0,1,1],
#         [0,1,0]]
#   print(rottenOrangeTime(arr))
    
        
        
#         R,C = len(grid),0
#         if not R:
#             C = len(grid[0])
            
#     def dfs(self,grid,i,j,r,c,level):
#         if not valid_point(i,j,r,c):
#             return 
#         if grid[i][j] == 0:
                    
            
#         if grid[i][j] == 1:
#             grid[i][j] == level
            
#         if grid[i][j] == 2:
#             self.dfs()
    
    
#     def valid_point(self,i,j,r,c):
#         if  0 <= i < r and 0 <= j < c:
#             return True
#         return False
    
# def rottenOrangeTime(arr):
 
