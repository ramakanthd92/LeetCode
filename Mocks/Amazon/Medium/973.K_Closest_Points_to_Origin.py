import heapq
import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def euclidean_distance(x,y):
            return math.sqrt(x*x + y*y)
       
        
        L = []
        heapq.heapify(L)
        for (x,y) in points:
            if len(L) < K:
                dist = euclidean_distance(x,y)
                # if len(L) > 0:
                #     print dist, -1*L[0][0]
                heapq.heappush(L,(-1*dist,(x,y)))
            else:
                dist = euclidean_distance(x,y)
                #print dist, -1*L[0][0]
                if dist <= -1*L[0][0]:
                    heapq.heappop(L)
                    heapq.heappush(L,(-1*dist,(x,y)))
            #print L
        res = []
        for (l,(x,y)) in L:
            res.append([x,y])
        
        return res
            
            
        
