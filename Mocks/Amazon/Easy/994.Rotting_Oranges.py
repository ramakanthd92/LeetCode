class Solution(object):
    def orangesRotting(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        if not r:
            return -1
        c = len(matrix[0])
        if not c:
            return -1
        
        visited = [[ 0 for _ in range(c)] for _ in range(r)] 
        output = [[ 1000 for _ in range(c)] for _ in range(r)] 
        
        def bfs(i,j):
            dq = collections.deque()
            dq.append((i,j))
            level = 1
            visited_set = set()
            visited_set.add((i,j))
            output[i][j] = 0
            while (len(dq) > 0):
                dq_len = len(dq)
                #print dq
                for _ in range(dq_len):
                    (i,j) = dq.popleft()
                    for k,l in [(-1,0),(0,1),(1,0),(0,-1)]:
                        if not ((0 <= i+k < r) and (0 <= j+l < c)):
                            continue 
                        else:
                            if ((i+k,j+l) not in visited_set and \
                                matrix[i+k][j+l] == 1 and output[i+k][j+l] > level):
                                output[i+k][j+l] = level
                                visited_set.add((i+k,j+l))
                                dq.append((i+k,j+l))
                                #print i,k,j,l
                                #print i+k , j+l
               # print level
                level+=1
                       
        for i in range(r):
            for j in range(c):
                #print i,j
                if matrix[i][j] == 2:
                    visited = [[ 0 for _ in range(c)] for _ in range(r)] 
                    output[i][j] = 0       
                    matrix[i][j] = -1             
                    bfs(i,j)
                    matrix[i][j] = 0            
      
                #print output
    
        max_time = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    if max_time < output[i][j]:
                        max_time = output[i][j]
        
        if max_time == 1000:
            return -1
        return max_time
                
            
