#Runtime - 68 ms    Memory - 11.8 MB
class Solution(object):
    def __init__(self):
        self.visited = []
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        
        xlen  = len(image)
        ylen = len(image[0])

        if image[sr][sc] == newColor:
            return image
        
        self.visited = [[0 for j in xrange(ylen)] for i in xrange(xlen)]
        self.bfs(image, sr, sc, newColor,xlen,ylen)
        
        return image
    
    def bfs(self,image,si,sj,target,xlen,ylen):
        if (si < 0 or si >= xlen) or (sj < 0 or sj >= ylen):
            return 
        q = collections.deque()
        q.append([si,sj])
        original_value = image[si][sj]
        image[si][sj] = target
        self.visited[si][sj] = 1
        level = 0
        while (len(q) > 0):
            q_len = len(q)
            for _ in xrange(q_len):
                [x,y] = q.popleft()
                for (i,j) in [(-1,0),(1,0),(0,1),(0,-1)]:
                    if not ((i+x) < 0 or (i+x) >= xlen or (y+j) < 0 or  (y+j) >= ylen):
                        if not self.visited[i+x][y+j] and image[i+x][y+j] == original_value:
                            q.append([i+x,y+j])
                            self.visited[i+x][y+j] = 1
                            image[i+x][y+j] = target
        return
