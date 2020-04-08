# Runtime - 36 ms   Memory - 13.6 MB  

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums)
        
        i = 0
        j = 0
        
        while (i<N and j <N): 
            if nums[i] == 0:
                i += 1
                continue
            if i != j:
                nums[j] = nums[i]
            i += 1
            j += 1
        
        while (j < N):
            nums[j] = 0
            j += 1
        
        return nums
