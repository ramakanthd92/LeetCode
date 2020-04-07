# Runtime - 28 ms    Memory - 11.8 MB
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        
        min_so_far = L-1
        max_so_far = L-1
        
        i = L-2
        while(i >= 0 and nums[i] >= nums[i+1]):
            if nums[max_so_far] < nums[i]:
                max_so_far = i
            i -= 1
        
        min_so_far = max_so_far
        for j in range(L-1,i,-1):
            if(nums[j] > nums[i] and nums[j] < nums[min_so_far]):
                min_so_far = j
                
        def swap(a,b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        
        if i >= 0:
            swap(i,min_so_far)
            
        def reverse_elements(i,j):
            while(i < j):
                swap(i,j)   
                i += 1
                j -= 1
    
        reverse_elements(i+1,L-1)
        
        return nums
        
        
