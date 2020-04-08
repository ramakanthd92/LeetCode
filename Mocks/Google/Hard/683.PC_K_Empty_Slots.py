class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        inc_stk = list()
        dec_stk = list()
        
        N = len(bulbs)
        
        for i in range(N):
            while(len(inc_stk) > 0 and inc_stk[-1] > bulbs[i]):
                val = inc_stk.pop()
            
            if len(inc_stk) > 0 and abs(inc_stk[-1] - bulbs[i])-1 == K:
                return i+1
            
            inc_stk.append(bulbs[i])
            
            while(len(dec_stk) > 0 and dec_stk[-1] < bulbs[i]):
                val = dec_stk.pop()
    
            if len(inc_stk) > 0  and abs(inc_stk[-1] - bulbs[i])-1 == K:
                return i+1
            
            dec_stk.append(bulbs[i])
            
        return -1
