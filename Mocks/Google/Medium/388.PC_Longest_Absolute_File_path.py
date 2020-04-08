import collections

class Solution(object):
    def __init__(self):
        self.root = collections.defaultdict(list)
        self.root["#"] = []
        self.local_dict = collections.defaultdict()
        self.max_length = 0
        
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        def count_tabs(word):
            count = 0
            for i in range(len(word)):
                if word[i] == "\t":
                    count += 1
                else:
                    break
            return count, word[i:]
                         
        def buildTree(input):
            dir_arr = input.split("\n")
                         
            self.local_dict = collections.defaultdict()
            self.local_dict[-1] = "#"
            
            for n in dir_arr:
                cnt,word = count_tabs(n)
                #print cnt,word
                self.local_dict[cnt] = word
                self.root[self.local_dict[cnt-1]].append(word)
        
        def find_max_length(rootword):
            #print rootword
            if not len(rootword):
                return 0
            if rootword not in self.root:
                if '.' in rootword:
                    return len(rootword)+1
                else:
                    return -1
                
            l = 0
            res = 0
            for n in self.root[rootword]:
                res = find_max_length(n)
                if res != -1:
                    l = max(l, find_max_length(n))
            
            #print rootword
            #print l
            if res < 0:
                return -1
            return l + len(rootword) + 1
            
        buildTree(input)
       # print self.root
        
        output = find_max_length("#")
        if output < 0:
            return 0
        return find_max_length("#")-3
    
    
        #print self.local_dict
        
