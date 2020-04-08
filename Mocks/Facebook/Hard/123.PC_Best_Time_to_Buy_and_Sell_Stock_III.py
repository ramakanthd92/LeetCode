class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
         
        def profit(prices):
            max_profit = 0
            N = len(prices)
            if N == 0:
                return 0
            min_price = float("inf")
            for i in range(N):
                if prices[i] < min_price:
                    min_price = prices[i]
                elif prices[i]-min_price > max_profit:
                    max_profit = prices[i]-min_price
            return max_profit
    
        max_profit = 0
        N = len(prices)
        if N == 0:
            return 0
        for i in range(N):
            max_profit = max(max_profit,profit(prices[:i]) + profit(prices[i:]))
            
        return max_profit
