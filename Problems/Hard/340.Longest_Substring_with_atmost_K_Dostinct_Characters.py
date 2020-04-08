# Runtime - 204 ms    Memory - 13.3 MB

from collections import Counter

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d1 = Counter()
        N = len(s)
        max_len = 0
        if not N:
            return 0
        l = 0
        r = 0
        d1[s[r]] += 1
        
        while (l < N and r < N):
            if len(d1) <= k:
                max_len = max(max_len,r-l+1)
                r+=1
                if r < N:
                    d1[s[r]] +=1
            elif len(d1) > k:
                d1[s[l]] -= 1
                if d1[s[l]] == 0:
                    del d1[s[l]]
                l += 1
                
        return max_len
        
