class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        container=set()
        i = j = result = 0
        sz = len(s)
        
        while i < sz and j < sz:
            if s[j] in container:
                container.remove(s[i])
                i += 1
            else:
                container.add(s[j])
                j += 1
                result = max(result, j-i)
        return (result)
        
        