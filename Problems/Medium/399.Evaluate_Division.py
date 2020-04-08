#Runtime - 16 ms     Memory - 13 MB
import collections  

class Solution(object):
    def __init__(self):
        self.found = False
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        hash_map = collections.defaultdict(list)
        N = len(equations)
        
        def dfs(source,target,level,values):
            if source not in hash_map:
                values[level] = 1.0
                return 1
            if source == target:
                values[level] = 1.0
                self.found = True
                return 1
            visited[source] = True
            
            for v,w in hash_map[source]:
                if not visited[v]:
                    values[level] = w
                  #  print w,source,v,level,values
                    dfs(v,target,level+1,values)
                    
                if self.found:
                    return
                
        for i in range(N):
            hash_map[equations[i][0]].append([equations[i][1],values[i]])
            hash_map[equations[i][1]].append([equations[i][0],1.0/values[i]])
        
        Q = len(queries)
        
        def calculate(values):
            res = 1.0
            for v in values:
                res *= v
            return res
            
        H = len(hash_map.keys())
        res = []
        for q in queries:
            values = [1.0 for i in range(H+1)]
            visited = collections.defaultdict(bool)
            for a in hash_map.keys():
                visited[a] = False
          #  print q
            self.found = False
            dfs(q[0],q[1],0,values)
            
            if self.found:
                res.append(calculate(values))
            else:
                res.append(-1.0)
        return res
