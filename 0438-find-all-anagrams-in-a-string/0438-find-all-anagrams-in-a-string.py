class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        stop = len(p)-1
        stack = []
        
        count_s = Counter(s[start:stop])
        count_p = Counter(p) 
        
        for i in range(stop,len(s)):
            
            first_letter = s[i-stop]
            last_letter = s[i]
            
            count_s[last_letter]+=1
            
            if count_s == count_p:
                
                stack.append(i-stop)
                
            if count_s[first_letter] == 1:
                
                del count_s[first_letter]
            else:
                count_s[first_letter] -= 1
        return stack