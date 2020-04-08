# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

import collections

class Solution(object):
    def __init__(self):
        self.hash_map = collections.defaultdict(bool)
        self.count = 0
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        
        while (hi - lo > 1):
            mid = lo + (hi-lo)/2
            #print lo,hi,mid
            if not self.checkBadVersion(mid) and self.checkBadVersion(mid+1):
                return mid+1
            elif self.checkBadVersion(mid):
                hi = mid
            elif not self.checkBadVersion(mid):
                lo = mid+1
            #print lo,hi,mid
         
        #print count
        #print self.hash_map
        #print lo,hi
        if lo == hi and self.checkBadVersion(lo):
            return lo
        if self.checkBadVersion(lo):
            return lo
        if self.checkBadVersion(hi):
            return hi
        return -1
        
    def checkBadVersion(self,m):
        if m not in self.hash_map:
            self.count += 1
            self.hash_map[m] = isBadVersion(m)
        return self.hash_map[m]
