import collections

class Solution(object):
    def __init__(self):
        self.long_palin_len = 0
        self.long_palin_hash = collections.defaultdict(list)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
         
        def extend_odd(i):
            j = 0
            #print i
            while (j <= i and i+j < L):
                if (s[i-j] == s[i+j]):
                    if self.long_palin_len < (2*j+1):
                        self.long_palin_len = 2*j+1
                        self.long_palin_hash[self.long_palin_len].append(s[i-j:i+j+1])  
                    j+=1
                else:
                    break
            
        def extend_even(i):
            j = 0
            #print i
            while (j <= i and i+j+1 < L):
                if (s[i-j] == s[i+j+1]):
                    if self.long_palin_len < (2*j+2):
                        #print j, i, i+j+1, L
                        self.long_palin_len = 2*j+2
                        self.long_palin_hash[self.long_palin_len].append(s[i-j:i+j+2]) 
                    j+=1
                else:
                    break
            
        
        L = len(s)
        if L == 0:
            return ""
              
        for i in range(L):
            extend_odd(i)
            extend_even(i)
            
       # print self.long_palin_hash
        
        if self.long_palin_len == 0:
            return ""
        return self.long_palin_hash[self.long_palin_len][0]
