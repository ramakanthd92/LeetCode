# Runtime - 4544 ms      Memory - 17.3 MB
import collections

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(list)
        
        i = 0
        for acct in accounts:
            graph[i] = acct
            i += 1
            
        N = i
        visited = [False for i in range(N)]
           
        def bfs(i):
            dq = collections.deque()
            dq.append(i)
            visited[i]  = True
            nodes = []
            nodes.append(i)
            
            while (len(dq) > 0):
                node = dq.popleft()
                for j in range(N):
                    if not visited[j]:
                        if set(graph[node][1:]).intersection(set(graph[j][1:])):
                            dq.append(j)
                            visited[j] = True
                            nodes.append(j)
            return nodes
        
        def process_nodes(nds):
            res_set = set()
            for j in nds:
                for k in graph[j][1:]:
                    res_set.add(k)
            
            res_list = sorted(list(res_set))
            #print res_list, 
            res_list = [graph[nds[0]][0]] +  res_list
            return res_list
            
        res = []
        for i in range(N):
            if not visited[i]:
                nodes = bfs(i)
                res.append(process_nodes(nodes))
                
        return res
