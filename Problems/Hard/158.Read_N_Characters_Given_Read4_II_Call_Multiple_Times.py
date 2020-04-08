# Runtime - 12 ms  Memory - 11.7 MB
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.local_buf = ['']*4
        self.st = -1
        self.en = -1
        self.has_content = False
        self.eof = False
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        def copy(sb,slb,p):
            #print sb,slb,p
            for i in range(p): 
                buf[sb+i] = self.local_buf[slb+i]
         
        def read_helper(n,st_buf):
            eof = False
            count = 0
            s = st_buf
            k = 0
            p = 0
            while (not eof and count < n):
                #print count
                #count = 0
                k = read4(self.local_buf)
                eof = (k != 4)
                p = min(n-count,k)
                copy(s,0,p)
                count += k            
                s += k

            if count == n:
                #print "n", n
                return n
            
            if count > n:
                self.has_content = True
                self.st = p
                self.en = k
                #print "k", n
                #print self.has_content,self.st,self.en
                return n
            
            if eof:
                #print "c", min(n,count)
                return min(n,count)
        
       # p = 0
        
        if not self.has_content:
            return read_helper(n,0)
        else:
            rem_buf_len = self.en-self.st
            if n < rem_buf_len:
                copy(0,self.st,n)
                self.has_content = True
                self.st += n
                return n 
            
            elif n == rem_buf_len:
                copy(0,self.st,n)
                self.has_content = False
                return n 
            
            else:
                copy(0,self.st,rem_buf_len)
                self.has_content = False
                return rem_buf_len + read_helper(n-rem_buf_len,rem_buf_len)
