import collections

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if not len(words):
            return True
        
        if not order:
            return True
        
        def compare_words(word1,word2):
            i = 0
            j = 0
            while (i < len(word1) and j < len(word2)):
                if word1[i] != word2[j]:            
                    if hash_map[word1[i]] > hash_map[word2[i]]:
                        return False
                    return True
                i+=1
                j+=1
            
            if i < len(word1):
                return False
            
            return True
        
        hash_map = collections.defaultdict(int)
        
        for i,c in enumerate(order):
            hash_map[c] = i
            
        for k in range(len(words)-1):
            if not compare_words(words[k],words[k+1]):
                return False
        
        return True
