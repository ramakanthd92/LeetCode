class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        S = S.upper()
        
        L = len(S)
        if L == 0:
            return ""
        
        if K == 0:
            return ""
        
        output = ""
        i = 0
        for j in range(L-1,-1,-1):
            #print S[j]
            if i < K:
                if S[j] != '-':
                    output += S[j]
                    i += 1     
            else:
                if S[j] != '-':
                    output += '-'
                    output += S[j]
                    i = 0
                    i += 1
                    
            #print output
                
        return "".join(reversed(output))
