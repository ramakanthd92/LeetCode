import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hash_map = collections.defaultdict(int) 
        
        N = len(s)
        l,r = 0,0
        
        max_len = 0
        
        while(l < N and r < N):
            if len(hash_map) <= k:
                hash_map[s[r]]+=1
                if len(hash_map) <= k:
                    #print l,r,s[l:r+1]
                    max_len = max(max_len, r-l+1)
                r+=1
            else:    
                hash_map[s[l]] -=1
                if hash_map[s[l]] == 0:
                    del hash_map[s[l]]
                l+=1
            
            
        
        return max_len
