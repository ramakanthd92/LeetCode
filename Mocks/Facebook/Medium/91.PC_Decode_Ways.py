class Solution(object):
    def numDecodings(self, nums):
        """
        :type s: str
        :rtype: int
        """
        
        # dp[i] = dp[i-1] + 1 if nums[i] > 2
        #         i+= 1
        #         dp[i-1] + 1 if nums[i+1] == 0 
        #         i += 2
        #         dp[i-1] + 2 if nums[i] == 1 or nums[i] == 2 and nums[i+1] <= 6
        #         i+=1
        #         dp[i-1] + 1 if nums[i] == 2 and nums[i+1] > 6
        #         i+=1
                
        N = len(nums)
        dp = [0 for i in range(N)]
        if nums[0] > '0':
            dp[0] = 1
        else:
            return 0
        for i in range(1,N):
            if nums[i] == '0' and nums[i-1] == '0':
                return 0
            elif nums[i] == '0': 
                dp[i] = dp[i-1]
            elif nums[i-1] == '1':
                dp[i] = dp[i-1] + 1
            elif nums[i-1] == '2' and '1' <= nums[i] <= '6':
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
                
        #print dp
        return dp[N-1]
