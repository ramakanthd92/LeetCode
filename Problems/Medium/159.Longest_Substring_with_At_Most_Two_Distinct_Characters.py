# Runtime - 52 ms   Memory - 13.1 MB

import collections

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        #LRU element
        hash_map = collections.defaultdict()
        
        N = len(s)
        l = 0
        r = 0
        max_len = 0
        
        while(r < N):
            if s[r] not in hash_map:
                hash_map[s[r]] =  1
            else:
                hash_map[s[r]] +=  1
                
            if len(hash_map) <= 2:
                max_len = max(max_len, r-l+1)
            else:
                while(l < N and len(hash_map) > 2):
                    if hash_map[s[l]] == 1:
                        del hash_map[s[l]]
                    else:
                        hash_map[s[l]] -= 1
                    l += 1
                    if len(hash_map) <= 2:
                        max_len = max(max_len, r-l+1)
            r+=1
        return max_len
        
