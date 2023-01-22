# import random
class Solution:
    def sortSentence(self, s: str) -> str:
        l =s.split()
        l.sort(key= lambda x: int(x[-1]))
        # l =''.join(lambda x: not x.isdigit(), s))
        
        return " ".join(x[:-1] for x in l)
        