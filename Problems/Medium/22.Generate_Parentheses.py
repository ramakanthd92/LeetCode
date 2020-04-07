# Runtime - 20ms  Memory - 12.8 MB

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res  = []
        def helper(open_br,close_br,path,n):
            if open_br > n or close_br > n:
                return
            if open_br == n and close_br == n:
               # print open_br,close_br,path
                res.append("".join(path))
                return
            if open_br >= close_br:
                    path.append('(')
                    helper(open_br+1,close_br,path,n)
                    path.pop()
                    
                    path.append(')')
                    helper(open_br,close_br+1,path,n)
                    path.pop()
        path = []
        helper(0,0,path,n)
        
        return res
