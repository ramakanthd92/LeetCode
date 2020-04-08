class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def bit_div(dividend,divisor):
            if dividend == divisor:
                return 0,1
            if dividend == 1:
                if dividend < divisor:
                    return 0,0
                else:
                    return 0,1
            elif divisor == 1:
                return 0,dividend
            
            k = divisor
            i = 1
            while k < dividend:
                k = k << 1
                i = i << 1
            m = k >> 1
            i = i >> 1
            return dividend-m, i
        
        neg = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True
            
        dividend, divisor =  abs(dividend), abs(divisor)
        rem_div = dividend
        quotient = 0
        
        while(rem_div > 0):
            rem_div,val = bit_div(rem_div,divisor)
            quotient += val
        
        MAX_INT = (1<<31)-1
        if quotient > MAX_INT:
            quotient = MAX_INT
        
        if neg:
            if quotient == MAX_INT:
                quotient += 1
            return -1*quotient
        return quotient
