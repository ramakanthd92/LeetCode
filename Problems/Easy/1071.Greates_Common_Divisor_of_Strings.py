# Runtime - 100 ms  Memory - 12.7 MB

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1Len = len(str1)
        str2Len = len(str2)
        
        if str1Len < str2Len:
            string = str1
        else:
            string = str2
            
        largeDivisor = ""
        
        for i in range(len(string)+1):
            s = string[:i]
            first = self.isDivisor(s,str1,0,len(str1),len(s))
            second = self.isDivisor(s,str2,0,len(str2),len(s))
            #print first, second, str1, str2, s
            
            if first and second:
                largeDivisor = s
            
        return  largeDivisor     
        
      
    def isDivisor(self,prefix,str3,i,strLen,prefixLen):
         
        if prefix == "":
            return True

       # print str3[i:], prefix 
        if strLen % prefixLen != 0: 
            return False
       
        j = 0
        while (j < prefixLen):
            if (prefix[j] != str3[i + j]):
                return False
            j += 1
        
        if prefixLen == strLen:
            return True
        
        return self.isDivisor(prefix,str3,i+j,strLen-prefixLen,prefixLen)
    
    
