# Runtime - 32 ms   Memory - 12.2 MB 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        L = len(nums)
        if not L:
            return -1
            
        def find_pivot():
            lo = 0
            hi = L-1
            while(lo < hi):
                mid = (lo+hi+1)/2
                if (mid+1 < L and nums[mid] > nums[mid+1]):
                    return mid+1
                elif (mid-1>=0 and nums[mid-1] > nums[mid]):
                    return mid    
                elif nums[mid] < nums[lo]:
                    hi = mid-1
                elif nums[mid] > nums[lo]:
                    lo = mid+1
                
            if lo == hi:
                return lo
            return 0
            
        def binary_search(l,h,target):
            lo = l
            hi = h
            while (lo < hi):
                mid = (lo + hi + 1)/2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid-1
                elif nums[mid] < target:
                    lo = mid+1
            if lo == hi and nums[lo] == target:
                return lo
            return -1
        
        p = find_pivot()
        lo = 0
        hi = L-1
        
        if nums[lo] > nums[hi]:
            if nums[0] <= target:
                return binary_search(0,p-1,target)
            else:
                return binary_search(p,L-1,target)
        return binary_search(0,L-1,target)
            
