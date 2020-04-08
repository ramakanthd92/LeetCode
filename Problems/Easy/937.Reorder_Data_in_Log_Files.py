# Runtime - 32 ms    Memory -12 MB
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_logs = []
        letter_logs = []
        for log in logs:
            boolean, log = self.is_digit_log(log)
            #print boolean,log
            if boolean:    
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort()
        formatted_letter_logs = []   
    
        for log in letter_logs:
            formatted_letter_logs.append(self.generate_letter_logs(log))
        
        return formatted_letter_logs + digit_logs
        
    def generate_letter_logs(self,words):
        log = words[-1]
        for word in words[0:-1]:
            log += ' '
            log += word
        return log      
    
    def is_digit_log(self,log):
        words = log.split(' ')
        #print words[1:]
       # print log
        for word in words[1:]:
            if self.is_letter(word):
                return False , words[1:] + [words[0]]
            if self.is_digit(word):
                return True, log
        return True, log
        
    def is_letter(self,word):
       # print word
        for l in word:
           # print l
            if not (ord(l) >= ord('a') and ord(l) <= ord('z')):
                return False
        return True
        
    def is_digit(self,word):
        for l in word:
            #print l
            if not(ord(l) >= ord('0') or ord(l) <= ord('9')):
                return False
        return True
