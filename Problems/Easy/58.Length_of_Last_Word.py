# Runtime - 16 ms   Memory - 11.8 MB

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        count = 0 
        temp_len = s_len-1
        if s=="":
            return 0
        while temp_len > -1 and s[temp_len] == " ":
            temp_len -= 1
        while s[temp_len] != ' ':
            if temp_len >= 0:
                count = count+1
            else:
                break
            temp_len -= 1
        return count
            

