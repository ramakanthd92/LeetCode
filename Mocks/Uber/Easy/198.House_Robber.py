class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if not L:
            return 0
        
        if L == 1:
            return nums[0]
        
        if L ==2:
            return max(nums[0], nums[1])
        
        dp = [0 for _ in range(L)] 
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2,L):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
        return dp[L-1]
