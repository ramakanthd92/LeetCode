from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        d1 = Counter(p)
        slen = len(s)
        plen = len(p)
        
        l = 0
        res = []
        d2 = Counter(s[:plen])
        while (l < slen-plen+1):
            if d1 == d2:
                res.append(l)
            d2[s[l]] -=1
            if d2[s[l]] == 0:
                del d2[s[l]]
            if l+plen < slen: 
                d2[s[l+plen]]+=1
            l+=1
            
        return res
