import heapq
import collections

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        W = len(workers)
        B = len(bikes)
        
        WB = list()
        
        distance_map = collections.defaultdict(list)
        
        def manhattan_dist(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        # creating a heap with all the pairs
        for i in range(W):
            for j in range(B):
                dist = manhattan_dist(workers[i],bikes[j])
                distance_map[dist].append(i,j)
                #heapq.heappush(WB,[dist,[i,j]])
                
        workers = [-1]*W
        bikes = [-1]*B
        
        #print WB
        
        # Loop till queue is not empty
        while(len(WB) > 0):
            pool = list()
            node = heapq.heappop(WB) # min node each time
            pool.append(node[1])
            while (len(WB) > 0 and WB[0][0] == node[0]):
                pool_node = heapq.heappop(WB)
                pool.append(pool_node[1])
            
            hash_map = collections.defaultdict(list)
            for [i,k] in pool:
                if i not in assigned_workers and \
                    k not in assigned_bikes:                                    
                    hash_map[i].append(k)
                    
            #print node[0], hash_map, assigned_workers,assigned_bikes
            for k in sorted(hash_map.keys()):
                for b in hash_map[k]:
                    if k not in assigned_workers and \
                        b not in assigned_bikes:
                        res[k] = b
                        assigned_workers.add(k)
                        assigned_bikes.add(b)
                        break
            #print res
        return res
#         w1 - b1
#         w1 - b2
        
#         w2 - b1
#         w2 - b2
        
#         w1 - list of all bikes with manhattan distances
#         w2 -
        
#         (W*B)
        
#         (w1,b1)
#          grt than
#         (w1,b2)
        
#         O(W*B)
        
#         manhattan dist
        
#         min_heap
        
#         PQ
#         - remove all pairs with the same distance
#         - which pair we need to take out
        
#         manhattan distane
#          - min worker
#          - min bike index
        
#         (w1,b1) - 
        
#         time - O(W*B)
#         space - O(W*B)
        
#         worker_set - worker
#         bike_set - bike
        
#         manhattan distances -> min heap -> sorted (minimum)
        
        
#         O(W*B)
        
#         T - O(W*B Log(W*B))
#         S - O(W*B + W + B)
        
