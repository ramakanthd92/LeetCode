import collections 

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) > len(nums2):
            return []
        
        hash_map_nums = collections.defaultdict()
        
        stk = list()
        num_len = len(nums2)
        
        for i in range(num_len):
            stk_len = len(stk)
            j = stk_len-1
            while (j >= 0 and stk[j] < nums2[i]):
                hash_map_nums[stk[j]] = nums2[i]
                stk.pop(j)
                j -= 1    
            stk.append(nums2[i])
        
        stk_len = len(stk)
        j = stk_len-1
        while (j >= 0):
            hash_map_nums[stk[j]] = -1
            stk.pop(j)
            j -= 1    
        
        res = []
        for n in nums1:
            if n in hash_map_nums:
                res.append(hash_map_nums[n])
            else:
                res.append(-1)
            
        return res
