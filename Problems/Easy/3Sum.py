# Runtime - 1580 ms    Memory - 15.1 MB

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        len_num = len(nums)
        res = set()
        for i in xrange(len_num):
            lo = i+1
            hi = len_num-1
            while lo < hi:
                if (nums[lo]+nums[hi]+nums[i] < 0):
                    while (lo+1 <= hi and nums[lo] == nums[lo+1]):
                        lo += 1
                    lo+=1
                elif (nums[lo]+nums[hi]+nums[i] > 0):
                    while(hi-1 >= lo and nums[hi] == nums[hi-1]):
                        hi -= 1
                    hi-=1
                else:
                    lis = [nums[lo],nums[hi],nums[i]]
                    lis.sort()
                    res.add((tuple)(lis))
                    
                    while( hi-1 >= lo and nums[hi] == nums[hi-1]):
                        hi -= 1
                    hi-=1
                    while (lo+1 <= hi and nums[lo] == nums[lo+1]):
                        lo += 1
                    lo+=1
        
        return res
