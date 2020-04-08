class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = len(prices)
        if not L:
            return 0
        
        min_so_far = [-1 for i in range(len(prices))]
        stack = list()
        len_stack = 0
        for i in range(L):
            while (len_stack > 0 and stack[len_stack-1] > prices[i]):
                stack.pop()
                len_stack -= 1 
            if len_stack == 0 or stack[len_stack-1] > prices[i]:
                stack.append(prices[i])
                len_stack += 1
            
            min_so_far[i] = stack[len_stack-1]
        
        #print min_so_far
        
        max_profit = 0
        for i in range(L):
            max_profit = max(prices[i]-min_so_far[i],max_profit)
        
        return max_profit
            
