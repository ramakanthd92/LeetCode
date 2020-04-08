from sys import maxint as MAXVAL
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1l = len(word1)
        w2l = len(word2)
        if not w1l and not w2l:
            return 0
        
        word1_pos = list()
        word2_pos = list()
        
        for i,w in enumerate(words):
            if w == word1:
                word1_pos.append(i)
            if w == word2:
                word2_pos.append(i)
                
        w1len = len(word1_pos)
        w2len = len(word2_pos)
        
        if not w1len or not w2len:
            return 0
        
        f,r = 0,0
        min_dist = MAXVAL
        while (f < w1len and r < w2len):
            min_dist = min(min_dist,abs(word1_pos[f] - word2_pos[r]))
            if (word1_pos[f] < word2_pos[r]):
                f += 1
            else:
                r += 1
        return min_dist
