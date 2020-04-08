# Runtime - 400 ms   Memory - 12.8 MB

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N = len(s)
        res = set()
        
        stk = []
        i = 0
        cnt = 0
        rem = 0
        while i < len(s):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                if cnt > 0:
                    cnt -=1
                else:
                    rem += 1
            i+=1
        rem += cnt
                    
        def backtrack(i,cnt,path):
            if cnt < 0:
                return 
            if len(path) > rem:
                return
            if i == N and cnt == 0 and len(path) == rem:
                past = 0
                str_res = []
                for k in path:
                    str_res.append(s[past:k])
                    past = k+1
                str_res.append(s[past:])
                res.add("".join(str_res))
            if i >= N:
                return 
            if s[i] == '(':
                path.append(i)
                backtrack(i+1,cnt,path)
                path.remove(i)
                backtrack(i+1,cnt+1,path)
            elif s[i] == ')':
                path.append(i)
                backtrack(i+1,cnt,path)
                path.remove(i)
                backtrack(i+1,cnt-1,path)
            else:
                backtrack(i+1,cnt,path)
        path = []
        backtrack(0,0,path)
        return res
