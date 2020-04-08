# Runtime - 20 ms    Memory- 12.6 MB

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = list()
        N = len(s)
        def is_digit(c):
            if '0' <= c < '9':
                return True
            return False
        
        p = 0
        val = ""
        digit = False
        while(p < N):
            if s[p] == '[':
                stk.append(val)
                val = ""
                stk.append('[')
            elif s[p] == ']':
                if val:
                    stk.append(val)
                val = ""
                #stk.append(']')
                el = stk.pop()
                #print el
                temp = ""
                while(el != '['):
                    temp = el + temp
                    el = stk.pop()
                    #print temp
                num = stk.pop() 
                #print num
                stk.append(int(num)*temp)
            else:
                if is_digit(s[p]):
                    if not digit:
                        if val:
                            stk.append(val)
                        val = s[p]
                        digit = True
                    else:
                        val += s[p]
                        digit = True
                else:
                    val += s[p]
                    digit = False
            p += 1
        
        stk.append(val)
       # print stk
        return "".join(stk)
            
              
