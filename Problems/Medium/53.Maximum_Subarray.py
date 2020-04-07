# Runtime - 48 ms   Memory - 13.3 MB

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        N = len(nums)
        
        if not N:
            return 0
    
        i = 0
        max_overall = -float("inf")
        max_so_far = -float("inf")
        start = 0 
        end = 0
    
        while i < N:
            if nums[i] < 0:
                if max_so_far + nums[i] < 0:
                    start = i+1
                    max_so_far = nums[i]
                else:
                    max_so_far += nums[i]
            else:
                if max_so_far < 0:
                    max_so_far = nums[i]
                else:
                    max_so_far += nums[i]
            if max_overall < max_so_far:
                max_overall = max_so_far
                end = i
            i += 1     
        
        return max_overall
        

