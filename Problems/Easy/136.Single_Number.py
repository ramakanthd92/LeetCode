# Runtime - 72 ms Memory - 14.6 MB

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_val = 0
         
        for n in nums:
            num_val = num_val ^ n
            
        return num_val
        
