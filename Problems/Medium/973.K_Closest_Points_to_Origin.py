# Runtime - 660 ms    Memory -18.6 MB

import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        point_list = []
        def eucl_dist(point):
            return sqrt(point[0]*point[0] + point[1]*point[1])
        
        
        for i in range(len(points)):
            #print point_list
            if len(point_list) < K:
                heapq.heappush(point_list,[-1*eucl_dist(points[i]),points[i]])     
            else:
                #print -1*eucl_dist(points[i]),  point_list[0]
                if point_list[0][0] < -1*eucl_dist(points[i]):
                    heapq.heappop(point_list)
                    heapq.heappush(point_list,[-1*eucl_dist(points[i]),points[i]])
        
        #print point_list
        res = []
        for k in range(len(point_list)):
            res.append(point_list[k][1])
            
        return res
