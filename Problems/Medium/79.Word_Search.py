# Runtime - 392 ms  Memory - 15.1 MB

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        M = len(board)
        N = len(board[0])
        K = len(word)
        visited = set()
        
        def valid_coords(i,j,k):
            if (i < 0 or i >= M) or (j < 0 or j >= N):
                return False
            if k < 0 or k >= K:
                return False
            return True
        
        def dfs(i,j,word,k):
            if not valid_coords(i,j,k):
                return False
            if word[k] != board[i][j]:
                return False
            if k == K-1 and word[k] == board[i][j]:
                #print i,j,k
                return True
            visited.add((i,j))
            l,r,u,d= False, False,False,False
            if valid_coords(i+1,j,k+1):
                if word[k+1] == board[i+1][j] and (i+1,j) not in visited:
                    if dfs(i+1,j,word,k+1):
                        visited.remove((i,j))
                        return True
            if valid_coords(i-1,j,k+1) and (i-1,j) not in visited:
                if word[k+1] == board[i-1][j]:
                    if dfs(i-1,j,word,k+1):
                        visited.remove((i,j))
                        return True
            if valid_coords(i,j+1,k+1) and (i,j+1) not in visited:
                if word[k+1] == board[i][j+1]:
                    if dfs(i,j+1,word,k+1):
                        visited.remove((i,j))
                        return True
            if valid_coords(i,j-1,k+1) and (i,j-1) not in visited:
                if word[k+1] == board[i][j-1]:
                    if dfs(i,j-1,word,k+1):
                        visited.remove((i,j))
                        return True
            visited.remove((i,j))
            return False
         
            
        for i in xrange(M):
            for j in xrange(N):
                if board[i][j] == word[0]:
                    if dfs(i,j,word,0):
                        return True
