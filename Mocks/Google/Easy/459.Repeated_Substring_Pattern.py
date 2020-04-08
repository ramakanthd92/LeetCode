class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)
        if L == 0:
            return False
        
        i = 0
        while i < L:
            j = i+1
            #print i,s[0:i+1] , s[j:j+i+1], j+i+1
            while (j+i <= L and s[0:i+1] == s[j:j+i+1]):
                j += (i+1)
                #print j
                if (j == L):
                    return True
            i += 1 
    
        return False 
        
        
