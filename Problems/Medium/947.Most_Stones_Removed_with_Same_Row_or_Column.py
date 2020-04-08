# Runtime - 140 ms    Memory - 15.1 MB

import collections

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        x_map = collections.defaultdict(list)
        y_map = collections.defaultdict(list)
        point_map = set()
        
        def dfs(x,y):
            x_nei = x_map[x]
            y_nei = y_map[y]
            
            if (x,y) in point_map:
                point_map.remove((x,y))
                
            for node in x_nei:
                if node in point_map:
                    dfs(node[0],node[1])
            for node in y_nei:
                if node in point_map:
                    dfs(node[0],node[1])
                    
        for s in stones:
            x_map[s[0]].append(tuple(s))
            y_map[s[1]].append(tuple(s))
            point_map.add(tuple(s))
        
        count = 0
        while(len(point_map) > 0):
            node = point_map.pop()
            dfs(node[0],node[1])
            count += 1
            
        return len(stones)-count
            
            
