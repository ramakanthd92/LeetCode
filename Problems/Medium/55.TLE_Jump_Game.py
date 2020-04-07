class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        if N == 0:
            return 0
        dp = [False for _ in range(N)]
    
        dp[N-1] = True 
         
        for i in range(N-2,-1,-1):
            j = 1
            while(i+j < N and j <= nums[i]):
                if dp[i+j]:
                    dp[i] = True
                    break
                j += 1
        
        #print dp
        return dp[0]
