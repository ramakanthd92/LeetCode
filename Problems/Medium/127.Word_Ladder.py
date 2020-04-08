# Runtime - 252 ms   Memory - 16.2 MB

import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if len(wordList) == 0:
            return 0
        if endWord not in wordList:
            return 0
        
        all_combo_dict = collections.defaultdict(list)
        
        length = len(wordList[0])
        
        # Pre-Processing for all generic word combinations
        for word in wordList:
            for i in xrange(length):
                gen_word = "".join(word[:i] + '*' + word[i+1:])
                all_combo_dict[gen_word].append(word)
            
        print all_combo_dict
        
        q = collections.deque()
        
        visited = {}
        
        q.append(beginWord)
        visited[beginWord] = 1
        level = 1
        while(len(q) > 0):
            len_q = len(q)
            level += 1
            for i in xrange(len_q):
                word = q.popleft()
                # Find all neighbours of this word
                for i in xrange(length):
                    gen_word = "".join(word[:i] + '*' + word[i+1:])
                    if gen_word in all_combo_dict:
                        for neighbour_word in all_combo_dict[gen_word]:
                            if neighbour_word not in visited:
                                q.append(neighbour_word)
                                visited[neighbour_word] = level
                                if neighbour_word == endWord:
                                    return level
        return 0;
        
        
