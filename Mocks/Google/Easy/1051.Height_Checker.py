class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        new_heights = sorted(heights)[:]
        
        N = len(heights)
        
        count = 0
        
        if not N:
            return 0
        
       # print new_heights
        
        for i in range(N):
            if heights[i] != new_heights[i]:
                count +=1
        
        return count
