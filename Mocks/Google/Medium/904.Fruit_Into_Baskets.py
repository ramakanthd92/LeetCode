class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        f,s,l = -1,-1,-1
        fe,se,le = -1,-1,-1
        max_win = 0
        
        L = len(tree)
        #print L
        for i,n in enumerate(tree):   
            if f < 0 or n == fe:
                f = i
                fe = n
                if l == -1:
                    max_win = max(max_win,f-l)
                else:
                     max_win = max(max_win,f-l)
                #print f,l
            elif s < 0 or n == se:
                s = i
                se = n
                if l == -1:
                    max_win = max(max_win,s-l)
                else:
                     max_win = max(max_win,s-l)
                #print s,l
            else:
                if n != fe and n != se:
                    if f < s:
                        l = f
                        le = fe
                        f = i
                        fe = n
                    else:
                        l = s
                        le = se
                        s = i
                        se = n
                    max_win = max(max_win, i-l)
            #print max_win
            
        #print f,s,l
       # print fe,se,le
            
        return max_win
                    
                    
            
