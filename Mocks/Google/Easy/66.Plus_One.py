class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        N = len(digits)
        
        if not N:
            return []
        
        rem = 0
        for i in range(N-1,-1,-1):
            if i == N-1:
                rem = 1    
            digi_sum = digits[i] + rem
            rem = digi_sum/10
            digits[i] = digi_sum % 10
            
        if rem:
            digits = [rem] + digits
        
        return digits
            
