# Runtime - 28 ms   Memory - 12.9 MB

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # Construct a Trie with Dictionary
        # check if it is possible 
        
        
       # recursive function 
       
       # s[j] = s[i] + w[i:j] exists 
       # use Trie DS 
       #
          
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]
