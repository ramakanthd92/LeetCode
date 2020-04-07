#Runtime - 64 ms  Memory - 14 MB

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        if not N:
            return [-1,-1]
        def left_search(nums,target):
            lo = 0
            hi = len(nums)-1
            
            while(lo < hi):
                mid = lo + (hi-lo)/2
                #print lo,hi,mid, nums[mid],target
                if nums[mid] == target:
                    if mid-1 >= 0 and nums[mid-1] < nums[mid]:
                        return mid
                    hi = mid
                   #print hi,mid
                elif nums[mid] > target:
                    hi = mid-1
                elif nums[mid] < target:
                    lo = mid+1
            
            if lo == hi and nums[lo] == target:
                return lo
            return -1
            
        def right_search(nums,target):
            lo = 0
            hi = len(nums)-1
            
            while(hi-lo > 1):
                #print lo,hi
                mid = lo + (hi-lo)/2
                if nums[mid] == target:
                    if mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                        return mid
                    lo = mid+1
                elif nums[mid] > target:
                    hi = mid-1
                elif nums[mid] < target:
                    lo = mid+1
                
            if nums[hi] == target:
                return hi
            elif nums[lo] == target:
                return lo
            return -1
            
        return [left_search(nums,target),right_search(nums,target)]
