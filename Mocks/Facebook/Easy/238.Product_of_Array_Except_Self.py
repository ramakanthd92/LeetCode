class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        if L == 0:
            return []
        
        l,r = 1,1
        left_arr = [0 for _ in range(L)]
        right_arr = [0 for _ in range(L)]
        for i in range(L):
            l = nums[i]*l
            left_arr[i] = l
            
        for j in range(L-1,-1,-1):
            r = nums[j]*r      
            right_arr[j] = r
            
        output = [1 for _ in range(L)]
        for k in range(L):
            if k == 0:
                if k+1 < L:
                    output[k] = right_arr[k+1]
            elif k == L-1:
                 if k >= 0:
                    output[k] = left_arr[k-1]
            else:
                output[k] = left_arr[k-1]*right_arr[k+1]
            
        return output
