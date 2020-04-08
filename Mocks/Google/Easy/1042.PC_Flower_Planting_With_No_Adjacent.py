import collections

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        
        adj_list = collections.defaultdict(list)
        for i in range(len(paths)):
            adj_list[paths[i][0]].append(paths[i][1])
            adj_list[paths[i][1]].append(paths[i][0])
        
        #print adj_list
        
        def dfs(source,count,N):
            #print source,count,N,color_arr
            if count == N:
                return True
            nodes = adj_list[source]
            color_set = set()
            for n in nodes:
                if color_arr[n]:
                    color_set.add(color_arr[n])
                    
            visited[source] = True
            for i in range(1,5):
                #print source,color_set
                if i not in color_set:
                    color_arr[source] = i
                    for n in nodes:
                        if not visited[n]:
                            if dfs(n,count+1,N):
                                return True 
                    if count+1 == N:
                        print color_arr
                        return True
            visited[source] = False
                
        color_arr = [0 for i in range(N+1)]    
        visited = [False for i in range(N+1)]
        
        for i in range(1,N+1):
            if not visited[i]:
                dfs(i,0,N)
        
        return color_arr[1:]
