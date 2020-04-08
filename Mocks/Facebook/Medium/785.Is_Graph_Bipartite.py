import collections

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        #print graph
        def bfs(node):
            dq = collections.deque()
            visited = set()
            dq.append(node)
            visited.add(node)
            color = 0
            hash_map[node] = color
            while(len(dq) > 0):
                n = dq.popleft()
                color = hash_map[n]
                color = (color + 1)%2
                for nei in graph[n]:
                    if nei not in visited:
                        visited.add(nei)
                        dq.append(nei)
                    if nei in hash_map:
                        if hash_map[nei] != color:
                            #print hash_map,hash_map[nei],color
                            #print nei,n
                            return False
                    else:
                         hash_map[nei] = color
            
            #print hash_map
            
            return True
        
        for i in range(len(graph)):
            hash_map = collections.defaultdict(int)
            # 0 - red
            # 1 - blue
            #print i
            #if len(graph[i]) == 0:
            #   return False
            if not bfs(i):
               # print i
                return False
        
        return True
