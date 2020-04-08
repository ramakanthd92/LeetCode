#Runtime - 44 ms Memory - 12.5 MB

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        L = len(prices)
        if not L:
            return 0
        
        min_till_now = sys.maxint
        max_profit = 0
        
        for p in prices:
            min_till_now = min(min_till_now,p)
            max_profit = max(max_profit, p - min_till_now)
            
        return max_profit
        
        
