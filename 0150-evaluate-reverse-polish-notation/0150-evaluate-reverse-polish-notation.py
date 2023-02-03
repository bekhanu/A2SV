class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for ch in tokens:
            if ch not in "+-/*":
                stk.append(int(ch))
            else:
                r, l= stk.pop(), stk.pop()
                if ch == "*":
                    stk.append(l *r)
                elif ch =="+":
                     stk.append(l +r)
                elif ch == "/":
                    stk.append(int(float(l)/r))
                elif ch== "-":
                    stk.append(l-r)
        return stk[-1]
                
            