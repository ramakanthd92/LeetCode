class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp = 0
        L = len(nums)
        sum_arr = [0 for _ in range(L+1)]
        
        for i in range(1,L+1):
            temp += nums[i-1]
            sum_arr[i] = temp
            
        count = 0
        for i in range(L+1):
            for j in range(i+1,L+1):
                if sum_arr[j]-sum_arr[i] == k:
                    count += 1
                    
        return count
