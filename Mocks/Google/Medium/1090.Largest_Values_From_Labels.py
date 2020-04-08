import heapq
import collections

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        pq = []
        hash_map = collections.defaultdict(int)
        
        for v,l in zip(values,labels):
            pq.append((-v,l))
        
        heapq.heapify(pq)
        
        num_used = 0
        total_sum = 0
        
        while(len(pq) > 0 and num_used < num_wanted):
            v,l = heapq.heappop(pq)
            if hash_map[l] < use_limit:
                total_sum += -1*v
                hash_map[l] += 1
                num_used += 1
        
        return total_sum
            
