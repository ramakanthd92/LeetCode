class Solution(object):
    def is_strobogrammatic(self,k):
        i = 0
        j = len(k)-1
        if k[i] == 0:
            return False
        while (i <= j):
            if (k[i] == 6 and k[j] != 9):
                return False
            elif (k[i] == 9 and k[j] != 6):
                return False
            elif k[i] != 6 and k[i] != 9 and k[i] != k[j]:
                return False
            i+=1
            j-=1
        return True
        
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # All same - 1,8
        # Palindrome - 1,8 at all positions 0 not in first position
        # rotatable - 6,9 at ends and middle different elements
        
        #hash_map = {0:[1,8],1:[1,0,8,6,9]}
        
        if n == 0:
            return []
        
        if n == 1:
            return ["0","1","8"]
       
        res = []
        
        
        def helper(i,n,num):
            if i == n:
                #print num
                if self.is_strobogrammatic(num):
                    #print num
                    res.append("".join([str(n) for n in num]))
                return
            
            # 0 1 2 3 4 
            # 5 -1 
            
            for k in [0,1,8,6,9]:
                if k == 0 and i == 0:
                    continue
                if i > n/2 and num[n-1-i] in [0,1,8] and k != num[n-1-i] :
                    continue
                if i > n/2 and num[n-1-i] in [6,9] and k in [6,9] and k == num[n-1-i]:
                    continue
                    
                num.append(k)
                helper(i+1,n,num)
                num.pop()
        
        num = []
        helper(0,n,num)
        return sorted(res)

