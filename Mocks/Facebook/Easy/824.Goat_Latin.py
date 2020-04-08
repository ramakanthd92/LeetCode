class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(" ")
        
        new_words = []
        i = 1
        for word in words:
            if lower(word[0]) in ('a','e','i','o','u'):
                new_words.append(word + "ma")
            else:
                new_words.append(word[1:] + word[0] + "ma") 
                
            new_words[-1] = new_words[-1] + 'a'*i
            i+=1
        
        if not len(new_words):
            return []
        res = new_words[0]
        for word in new_words[1:]:
            res += " "
            res += word
            
        return res
