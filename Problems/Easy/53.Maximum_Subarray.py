from sys import maxint as MAXVAL
MIN_VAL = -(2<<30) 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if not L:
            return MIN_VAL
        
        max_sum = MIN_VAL
        lsum = MIN_VAL
        
        for i in xrange(L):
            #print i, lsum
            if nums[i] >= 0:
                if lsum < 0:
                    lsum = nums[i]
                else:
                    lsum += nums[i]
            elif nums[i] < 0:
                if lsum + nums[i] <= 0:
                    lsum = nums[i]
                elif lsum + nums[i] > 0:
                    lsum += nums[i]
                    
            if max_sum < lsum:
                max_sum = lsum
            print i, lsum, max_sum
            
        return max_sum
        
