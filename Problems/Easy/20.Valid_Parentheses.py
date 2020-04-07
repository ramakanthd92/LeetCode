# Runtime - 24 ms    Memory - 12 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)
        if L == 0:
	        return True
        stk = list()
        i  = 0
        while (i < L):
            if s[i] == '(' or  s[i] == '[' or  s[i] == '{':
                stk.append(s[i])
            else:
                if len(stk) == 0:
                    return False
                if s[i] == ')' and stk[-1] != '(':
                    return False
                if s[i] == ']' and stk[-1] != '[':
                    return False
                if s[i] == '}' and stk[-1] != '{':
                    return False
                stk.pop()
            i+=1     
        if len(stk) > 0:
            return False
        return True

        

