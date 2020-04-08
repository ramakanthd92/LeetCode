# Runtime - 100 ms   Memory - 11.8 MB

from sys import maxint as MAX_VALUE

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        len_num = len(nums)
        close_diff = MAX_VALUE
        close_sum = 0
        for i in xrange(len_num):
            lo = i+1
            hi = len_num -1
            while (lo < hi):
                sum_val = nums[i]+nums[lo]+nums[hi]
                if sum_val < target:
                    if close_diff > abs(target - sum_val):
                        close_sum = sum_val
                        close_diff = abs(target - sum_val)
                        
                    while(lo+1 < hi and nums[lo] == nums[lo+1]):
                        lo+=1
                    lo+=1
                    
                elif nums[i]+nums[lo]+nums[hi] > target:
                    if close_diff > abs(target - sum_val):
                        close_sum = sum_val
                        close_diff = abs(target - sum_val)
                       
                    while(lo < hi-1 and nums[hi] == nums[hi-1]):
                        hi-=1
                    hi-=1
                    
                else:
                    if close_diff > abs(target - sum_val):
                        close_sum = sum_val
                        close_diff = abs(target - sum_val)
                    return close_sum 
        return close_sum
    
