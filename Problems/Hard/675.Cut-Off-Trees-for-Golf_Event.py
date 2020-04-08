# Runtime - 6892 ms  Memory - 12 MB

import collections
class Solution(object):
    
    def __init__(self):
        self.visited = None
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest:
            return -1
        xlen  = len(forest)
        ylen = len(forest[0])

        tree_heights = []
        
        for i in xrange(xlen):
            for j in xrange(ylen):
                if forest[i][j] != 0 and forest[i][j] != 1:
                    tree_heights.append(forest[i][j])
        
        tree_heights.sort()
        
        self.visited = [[0 for j in xrange(ylen)] for i in xrange(xlen)]
        
        #print xlen,ylen
        #print tree_heights
        
        res = 0
        l,m = 0, 0
        for o in xrange(len(tree_heights)):
            self.visited = [[0 for j in xrange(ylen)] for i in xrange(xlen)]
            dist, x, y = self.bfs(forest,l,m,tree_heights[o],xlen,ylen)
            #print tree_heights[o] , '->', dist, x, y
            if dist == -1:
                return -1
            else:
                res += dist
                l,m = x,y   
                
        return res
        
    def bfs(self,forest,si,sj,target,xlen,ylen):
        if (si < 0 or si >= xlen) or (sj < 0 or sj >= ylen):
            return -1, -1, -1
        if forest[si][sj] == target:
            return 0, si, sj
        q = collections.deque()
        q.append([si,sj])
        self.visited[si][sj] = 1
        level = 0
        while (len(q) > 0):
            q_len = len(q)
            for _ in xrange(q_len):
                [x,y] = q.popleft()
                for (i,j) in [(-1,0),(1,0),(0,1),(0,-1)]:
                    if not ((i+x) < 0 or (i+x) >= xlen or (y+j) < 0 or  (y+j) >= ylen):
                        if not self.visited[i+x][y+j] and forest[i+x][y+j] != 0:
                            q.append([i+x,y+j])
                            self.visited[i+x][y+j] = 1
                            if forest[i+x][y+j] == target:
                                return level+1, i+x, y+j
            level += 1
        return -1, -1, -1
                         
