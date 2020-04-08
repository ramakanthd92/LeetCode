# Runtime - 508 ms   Memory- 13.7 MB 
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        hash_map = {}
        
        def hours_needed(k):
            count = 0
            for p in piles:
                count += (p-1)/k+1
            return count <= H
        
        lo = 1
        hi = max(piles)
        while (lo < hi):
            mid = lo + (hi-lo)/2
            if not hours_needed(mid):
                lo = mid+1
            else:
                hi = mid
                
        return lo
