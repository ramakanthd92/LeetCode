import collections

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        
        hash_map = collections.defaultdict(int)
        
        for i in range(len(keyboard)):
            hash_map[keyboard[i]] = i
            
        i = 0
        L = len(word)
        res = 0
        last = 0
        while (i < L):
            curr = hash_map[word[i]]
            #print word[i],curr
            res += abs(curr-last)
            last = curr
            i+= 1
            
        return res
