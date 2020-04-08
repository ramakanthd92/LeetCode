# Runtime - 1352 ms      Memory - 12 MB

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        if not len(coins):
            return -1
        dp = [0 for i in range(amount+1)]
        
        dp[0] = 0
        
        for i in range(amount+1):
            for c in coins:
                if i-c == 0 or (i-c > 0 and dp[i-c]):
                    if dp[i] > 0:
                        dp[i] = min(dp[i-c]+1, dp[i])
                    else:
                        dp[i] = dp[i-c] + 1
        
        #print dp
        if dp[amount] == 0:
            return -1
        return dp[amount]
