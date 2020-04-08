class Solution(object):
    def isStrobogrammatic(self, s):
        """
        :type num: str
        :rtype: bool
        """
        
        l = 0
        r = len(s)-1
        
        if len(s) == 0:
            return True
        
        while (l<=r):
            if s[l] == '6' and s[r] != '9':
                return False
            elif s[l] == '9' and s[r] != '6':
                return False
            elif s[l] in ('1','0','8') and s[l] != s[r]:
                return False
            elif s[l] in ('2','3','4','5','7') or s[r] in ('2','3','4','5','7'):
                return False
            l+=1
            r-=1
            
        return True
