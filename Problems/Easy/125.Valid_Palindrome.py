# Runtime - 400ms   Memory - 17.1 MB

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not len(s):
            return True
        
        
        def strip_spaces(string):
            sub_str = ""
            for i in range(len(string)):    
                if 'a' <= string[i] <= 'z' or '0' <= string[i] <= '9':
                    sub_str += string[i] 
                elif 'A' <= string[i] <= 'Z':
                    sub_str += chr(ord('a') + (ord(string[i]) - ord('A')))  
                    
            return sub_str
        
        def is_palindrome(string):
            N = len(string)
            # 5 -> 0,1,2
            # 4 -> 0,1
            if N == 0:
                return True
            for i in range((N+1)/2):
                if string[i] != string[N-1-i]:
                    return False
            return True
        
        sub_str = strip_spaces(s)
        
        return is_palindrome(sub_str)
