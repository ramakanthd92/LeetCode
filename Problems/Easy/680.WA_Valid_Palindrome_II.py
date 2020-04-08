# Runtime -    Memory -

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        
        
        l = 0
        r = N-1
        
        deleted = 0
        
        while(l < r and deleted < 2):
            if s[l] != s[r]:
                if deleted >= 1:
                    return False
                if s[l] == s[r-1]:
                    r -= 1
                    deleted += 1
                elif s[l+1] == s[r]:
                    l += 1
                    deleted += 1
                else:
                    return False
            else:
                l+=1
                r-=1
                
        if deleted >=  2:
            return False
        
        return True
