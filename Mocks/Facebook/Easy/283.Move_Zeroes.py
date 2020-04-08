class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r = 0,0
        N = len(nums)
        while (l < N and r < N):
            if nums[r] == 0:
                r += 1
            else:
                if l != r:
                    nums[l] = nums[r]
                l+=1 
                r+=1
        
        while (l < N):
            nums[l] = 0
            l+=1
        
        return nums
