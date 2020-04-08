#Runtime - 12 ms  Memory - 11.8 MB

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        
        
        st = lower
        en = upper 
        
        L = len(nums)
        
        res = []
        
        if L == 0:
            lo = lower
            up = upper 
            if up-lo > 0:
                    res.append(str(lo) + "->" + str(up))
            elif up-lo == 0:
                res.append(str(lo))
        
            return res
        
        
        
        for i in range(-1,L,1):
            #print i
            if i == L-1:
                lo = nums[i]
                up = upper 
                if up-lo > 1:
                    res.append(str(lo+1) + "->" + str(up))
                elif up-lo == 1:
                    res.append(str(lo+1))
            elif i == -1:
                lo = lower
                up = nums[i+1]
                if up-lo > 1:
                    res.append(str(lo) + "->" + str(up-1))
                elif up-lo == 1:
                    res.append(str(lo))
            else:
                lo = nums[i]
                up = nums[i+1]
                if up-lo > 2:
                    res.append(str(lo+1) + "->" + str(up-1))
                elif up-lo == 2:
                    res.append(str(lo+1))
            #print lo,up
            
                
        return res
