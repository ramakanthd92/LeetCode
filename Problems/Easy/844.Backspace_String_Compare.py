# Runtime - 20 ms  Memory - 11.8 MB

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        N = len(S)
        M = len(T)
        
        n = N-1
        m = M-1

        while (n >= 0 or m >= 0):
            skip = 0
            while n >= 0:
                if S[n] == '#':
                    n -= 1
                    skip += 1
                elif skip > 0:
                    skip -= 1
                    n-=1
                else:
                    break
        
            skip = 0
            while m >= 0:
                if T[m] == '#':
                    m -= 1
                    skip += 1
                elif skip > 0:
                    skip -= 1
                    m-=1
                else:
                    break
                    
            #print n,m, S[n],T[m]
            if n >= 0 and m >= 0 and S[n] != T[m]:
                return False
            if (m >= 0) !=  (n >= 0):
                return False
            
            n -= 1
            m -= 1
            
        return True
