import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s2) < len(s1):
            return False
        
        sorted_str = "".join(sorted(s1))
        s1_len = len(s1)
        s2_len = len(s2)
        
        for i in range(s2_len-s1_len+1):
            #print "".join(sorted(s2[i:i+s1_len]))
            if "".join(sorted(s2[i:i+s1_len])) == sorted_str:
                return True
            
        return False
