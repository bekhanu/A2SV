class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        sl ={')': '(', '}':'{', ']':'['}
        for i in s:
            if i in sl:
                if stack and stack[-1] == sl[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                