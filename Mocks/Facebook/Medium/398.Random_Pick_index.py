import collections
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hash_map = collections.defaultdict(list)
        for i in range(len(nums)):
            self.hash_map[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        if target in self.hash_map:
            len_list = len(self.hash_map[target])
            r = random.randrange(len_list)
            #print self.hash_map[target]
            return self.hash_map[target][r]
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
