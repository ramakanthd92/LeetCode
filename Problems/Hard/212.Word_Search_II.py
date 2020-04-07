# Runtime - 948 ms   Memory - 36.8 MB

import collections

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        prefix_map = collections.defaultdict(set)
        
        R,C = len(board),0
        if R:
            C = len(board[0])
        else:
            return []
        
        res = []
        
        def preprocess(): 
            for w in words:
                for i in range(len(w)):
                    prefix_map[w[:i+1]].add(w) 
        
        def dfs_helper(i,j,level,path):
            if not (0 <= i < R and 0 <= j < C): 
                return 
            visited.add((i,j))                    
            path.append(board[i][j]) 
            #print '[',path,i,j,level,visited,']'
            found_word = ''.join(path)
            
            if found_word in prefix_map:
                if found_word in words:
                    res.append(found_word)
                    #print "found"
            elif found_word not in prefix_map:
                visited.remove((i,j))
                path.pop()
                return
            for d,e in [[1,0],[-1,0],[0,1],[0,-1]]:
                if (i+d,j+e) not in visited:
                    dfs_helper(i+d,j+e,level+1,path)
            path.pop()
            visited.remove((i,j))
                    
        preprocess()
        for i in range(R):
            for j in range(C):
                path = []
                visited = set()
                dfs_helper(i,j,0,path)
                
       # print res
       # print prefix_map
        
        return list(set(res))
