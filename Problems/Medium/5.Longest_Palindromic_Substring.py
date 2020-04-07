# Runtime - 5616 ms   Memory - 21.4 MB

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        if not L:
            return ""
        
        palin = [[False for i in range(L)] for j in range(L)] 
        start,end = -1,-1
    
        for i in range(L):
            palin[i][i] = True
            start,end= i,i
        
        for i in range(L-1):
            if s[i] == s[i+1]:
                palin[i][i+1] = True
                start,end = i,i+1
        max_palin_len = 0
        for k in range(2,L):
            for i in range(0,L-1):
                if i+k < L:
                    if s[i]==s[i+k] and palin[i+1][i+k-1]:
                        #print i,i+k,s[i:i+k+1]
                        palin[i][i+k] = True
                        max_palin_len = max(k+1,max_palin_len)
                        start = i
                        end = i+k
        
        if start < 0 and end < 0:
            return ""
        return s[start:end+1]
