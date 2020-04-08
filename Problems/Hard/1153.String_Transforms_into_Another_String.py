# Runtime - 16 ms   Memory - 13.1 MB

import collections

class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        
        hash_map = collections.defaultdict()
        
        L = len(str1)
        
        if L == 0:
            return true
        
        i = 0
        while (i < L):
            if str1[i] not in hash_map:
                hash_map[str1[i]] = str2[i]
            else:
                if hash_map[str1[i]] != str2[i]:
                    return False
            i += 1
        
        return len(set(str2)) < 26
                
        
