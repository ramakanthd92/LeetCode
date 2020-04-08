class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        N = len(S)
        
        M = ""
        
        start,end = N,N
        for i,s,t in zip(indexes,sources,targets)[::-1]:
            start = i+len(s)
            M = S[start:end] + M
            if S[i:i+len(s)] == s:
                M = t + M 
            else:
                M = S[i:i+len(t)] + M
            end = i
                
        print M
        return M
