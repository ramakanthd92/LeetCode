class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return -1
        L = len(nums)
        
        if L == 1:
            return 0
        
        lo = 0
        hi = L-1
        
        while (lo < hi):
            mid = (lo+hi+1)/2
            print lo, mid, hi
            if (mid == hi or mid == lo):
                break
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                lo = mid + 1
            elif  nums[mid-1] > nums[mid] > nums[mid+1]:
                hi = mid -1
            else:
                lo = mid+1
                
        
        #print lo, hi
        if lo-1 < 0 and lo+1 > L-1:
            return lo
        if hi-1 < 0 and hi+1 > L-1:
            return hi
        if lo-1 >= 0  and lo+1 <= L-1 and  nums[lo-1] < nums[lo] > nums[lo+1]:
            return lo
        if hi-1 >= 0  and hi+1 <= L-1 and  nums[hi-1] < nums[hi] > nums[hi+1]:
            return hi
        if lo-1 < 0 and nums[lo] > nums[lo+1]:
            return lo
        if hi+1 > L-1 and nums[hi-1] < nums[hi]:
            return hi      
        return -1
