# Runtime - 52 ms   Memory - 12 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = len(nums)
        if L == 0:
            return []
        lo = 0
        hi = L-1
        cursum = nums[lo] + nums[hi]
             
        while (lo < hi):
            if  cursum== target:
                return [lo+1,hi+1]
            elif cursum < target:
                lo+=1
            else:
                hi-=1
            cursum = nums[lo] + nums[hi]
            
        if lo != hi and cursum == target:
            return [lo+1,hi+1]
        return []
