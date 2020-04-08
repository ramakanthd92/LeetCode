# Runtime - 40 ms     Memory - 12.1 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        max_len = 0
        start = 0
        len_s = len(s)
        
        for i in xrange(0,len_s):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                if start <= dict[s[i]]:
                    start = dict[s[i]]+1
                    dict[s[i]] = i
                else:
                    dict[s[i]] = i
            if max_len < i-start+1:
                max_len = i-start+1
            
        return max_len
