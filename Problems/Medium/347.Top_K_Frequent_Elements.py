# Runtime - 76 ms    Memory - 15.4 MB

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        L = len(nums)
        hash_map = {}  
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                hash_map[n] += 1
        
        li = []
        
        for i,v in hash_map.items():
            li.append([-1*v,i])
        
        heapq.heapify(li)
        
        res  = []
        for i in xrange(k):
            res.append(heapq.heappop(li)[1])
        
        return res
            
