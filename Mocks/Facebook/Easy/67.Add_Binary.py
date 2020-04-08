class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        rem = 0
        ans = ""
        a_len = len(a)
        b_len = len(b)
        a = a[::-1]
        b = b[::-1]
        
        i = 0
        while(i < a_len or i < b_len):
            if i < a_len and i < b_len and a[i] == '1' and b[i] == '1':
                val = 2 + rem
            elif (i >= b_len or b[i] == '0') and i < a_len and a[i] == '1':
                val = 1 + rem
            elif (i >= a_len or a[i] == '0') and i < b_len and b[i] == '1':
                val = 1 + rem
            else:
                val = 0 + rem
            rem = val/2
            res = val%2
            ans = str(res) + ans
            i += 1
        
        if rem:
            ans = str(rem) + ans
            
        return ans
