class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        T = len(t)
        arr = [-1 for _ in range(S)]
        
        sp = 0
        tp = 0
        
        counter = 0
        
        while(sp < S and tp < T):
            if t[tp] == s[sp]:
                sp += 1
                counter += 1
            tp += 1
                
       # print counter 
        if sp == S and counter == S:
            return True
        
        return False
            
