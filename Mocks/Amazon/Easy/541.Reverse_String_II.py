class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        L = len(s)
        def reverse(s,i,k):
            if len(s)-i < k:
                l = len(s)-i
                for j in range(0,l/2,1):
                    swap(s,i+j,i+l-j-1)    
            else: 
                for j in range(0,k/2,1):
                    swap(s,i+j,i+k-j-1)
                    
        def swap(s,i,j):
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
        
        def split(word): 
            return [char for char in word]
        
        slist = split(s) 
        for i in range(0,L,2*k):
            reverse(slist,i,k)
            
        return "".join(slist)
        
