class Solution:
    def calculate(self, s: str) -> int:
        num =0
        stack =[]
        sign= "+"
        for i in s + "+":
            if i.isdigit():
                num=num*10 + int(i)
            elif i in "+-*/":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(math.trunc(stack.pop()/ num))
                    
                sign = i
                num =0
                
        return sum(stack)