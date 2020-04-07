# Runtime - 12 ms   Memory - 11.8 MB
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        N = len(digits)
        if not N:
            return []
        
        hash_map = { '2' : ['a','b','c'],
                     '3' : ['d','e','f'],
                     '4' : ['g','h','i'],
                     '5' : ['j','k','l'],
                     '6' : ['m','n','o'],
                     '7' : ['p','q','r','s'],
                     '8' : ['t','u','v'],
                     '9' : ['w','x','y','z']
                    }
        res = []
        def helper(i,n,path):
            if i > n:
                return 
            if i == n:
                res.append("".join(path))
                return
            #print digits[i]
            for k in hash_map[digits[i]]:
                path.append(k)
                helper(i+1,n,path)
                path.pop()
        
        path = []
        helper(0,N,path)
        return res
