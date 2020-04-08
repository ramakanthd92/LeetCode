class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cnt = 0
        i = 1
        while (i*i <= n):
            #print i*i
            i += 1
            cnt += 1
            
        return cnt
