class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        slow = 0
        fast = 0
        
        typed_len = len(typed)
        name_len = len(name)
        

        if not typed_len or not name_len:
            return False
    
        if typed_len < name_len:
            return False
    
        
        while (slow < name_len and fast < typed_len):
            slow_char = name[slow]
            slow_count = 0 
            while(slow < name_len and name[slow] == slow_char):
                slow += 1
                slow_count += 1
            
            fast_char = typed[fast]
            fast_count = 0
            while(fast < typed_len and typed[fast] == fast_char):
                fast += 1
                fast_count += 1
                
            if fast_char != slow_char:
                return False
            elif fast_count < slow_count:
                return False
        
        #print fast,slow,typed_len,name_len
        if (fast == typed_len and slow == name_len):
            return True
        
        return False
