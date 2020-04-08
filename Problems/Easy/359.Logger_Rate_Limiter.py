#Runtime - 148 ms    Memory - 19.3 MB

import collections
import threading

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = collections.defaultdict()
        self.lock = threading.Lock()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        with self.lock:
            if message not in self.hash_map:
                self.hash_map[message] = timestamp
                return True
            else:
                last_time = self.hash_map[message] 
                if (timestamp-last_time) < 10:
                    return False
                self.hash_map[message] = timestamp
                return True

        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
