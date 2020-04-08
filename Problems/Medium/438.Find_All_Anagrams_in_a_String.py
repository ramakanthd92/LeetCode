# Runtime - 284 ms   Memory - 13.7 MB  
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d1 = Counter(p)
        
        if len(s) < len(p):
            return []
        
        res = []
        slen = len(s)
        plen = len(p)
        d2 = Counter(s[0:plen])
        for i in range(slen-plen+1):
            if i > 0:
                d2[s[i-1]]-=1
                if d2[s[i-1]] == 0:
                    del d2[s[i-1]]
                d2[s[i+plen-1]]+=1
            if d1 == d2:
                res.append(i)
            
           # print d1,d2
        return res
