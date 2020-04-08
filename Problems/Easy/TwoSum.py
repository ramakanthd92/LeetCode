# Runtime - 36 ms   Memory - 13.3 MB
import collections

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {}
        num_len = len(nums)
        
        if num_len < 2:
            return []
        
        for i in xrange(0,num_len):
            dict[nums[i]] = i
        
        for j in xrange(0,num_len):
            k = (target - nums[j]) 
            if k in dict and j != dict[k]:
                return [j,dict[k]]
        
        return []
        
            
        
