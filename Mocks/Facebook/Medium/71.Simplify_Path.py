class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stk = list()
        
        dirs = path.split('/')

        for d in dirs:
            if d == "" or d == ".":
                continue
            elif d == "..":
                stk_len = len(stk)
                if stk_len >= 1:
                    stk.pop(stk_len-1)
            else:
                stk.append(d)
            
        cn = ""
        
        for p in stk:
            cn += "/"
            cn += p
        
        if cn == "":
            return "/"
            
        return cn
        
