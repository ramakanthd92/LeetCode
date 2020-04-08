import collections
import heapq

class Solution(object):    
    def __init__(self): 
        self.V = None 
        self.graph = None
  
    def printSolution(self, dist): 
        #print "Vertex \tDistance from Source"
        max_dist = 0
        for node in range(self.V): 
            max_dist = max(max_dist,dist[node])
            #print node, "\t", dist[node] 
        return max_dist
    
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxint 
        min_index = 0
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxint] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
            #print u
            #print sptSet
            #print dist
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                #print u,v,self.graph[u][v],dist[u],dist[v]
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v] 
  
        return self.printSolution(dist) 
    
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        self.V = N
        self.graph = [[0 for column in range(N)]  
                    for row in range(N)] 
        
        for (u,v,w) in times:
            #print u,v
            self.graph[u-1][v-1] = w

        #print self.graph
        return self.dijkstra(K-1)
        
        #self.printSolution(dist)
