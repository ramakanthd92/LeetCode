# Runtime - 44 ms    Memory - 12.8 MB

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        stk = []
        unbalanced_stk = []
        N = len(S)
        if not N:
            return 0
        i = 0
        while (i < N):
            if S[i] == '(':
                stk.append(i)
            else:
                if len(stk) > 0:
                    stk.pop()
                else:
                    unbalanced_stk.append(i)
            i += 1
            
        return len(unbalanced_stk) + len(stk)
