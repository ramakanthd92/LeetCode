class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {'I' : 1, 'V':5 , 'X': 10, 'L':50, 'C':100, 'D':500 ,'M':1000}
        
        i = 0
        output = 0
        while (i < len(s)):
            if i+1 >= len(s):
                output +=  hash_map[s[i]]
                i+= 1   
            else:
                if hash_map[s[i+1]] > hash_map[s[i]]:
                    output += (hash_map[s[i+1]] - hash_map[s[i]])
                    i+=2
                else:
                    output += hash_map[s[i]]
                    i+=1
                    
        return output
