# Runtime - 960 ms    Memory - 21.4 MB
import collections

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        
        def check(result,i):
            L = len(result)
            for k in range(i+1):
                for j in range(i+1):
                    if result[k][j] != result[j][k]:
                        return False
            return True
        
        def helper(w,i,word_len, result):            
            if not check(result,i):
                return
            if i == word_len-1:
                if check(result,i):
                    output.append(result[:])
                return
            
            prefix = ''
            for k in range(i+1):
                if result[k]:
                    prefix += result[k][i+1]
            
            for nei in hash_map[prefix]:
                result[i+1] = nei
                helper(nei,i+1,word_len,result)
                result[i+1] = ""
            
        W = len(words)
        if not W:
            return []
        word_len = len(words[0])
        
        hash_map = collections.defaultdict(list)
        for i in range(word_len):
            for w in words:
                hash_map[w[:i+1]].append(w)
            
        output = []
        
        result = ["" for _ in range(word_len)]
        
        for w in words:
            result[0] = w
            helper(w,0,word_len,result)
            result[0] = w
        return output
