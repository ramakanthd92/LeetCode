import collections

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        hash_map = collections.defaultdict(list)
        
        n , d = numerator, denominator
        neg = False
        
        if n == 0:
            return "0"
        if d == 0:
            return None
        if (n < 0 and d > 0) or (n > 0 and d < 0):
            neg = True
        
        n,d = abs(n),abs(d)
        
        dec = n/d
        
        m = n%d
        res = ""
        
        if not m:
            res = str(dec)
            if neg:
                return '-' + res
            return res
    
        fract = ""
        i = 0 
        while (m and m not in hash_map):
            m = m*10
            fract += str(m/d)
            hash_map[m/10] = i
            i += 1
            m = m%d
        
        index  = 0
        
        if m:
            if m in hash_map:
                index = hash_map[m]
            recur =  '(' + fract[index:i] + ')'
            res = str(dec) + "." + fract[:index] + recur                
        else:
            res = str(dec) + "." + fract
        
        if neg:
            return '-' + res
        return res
        
            
            
