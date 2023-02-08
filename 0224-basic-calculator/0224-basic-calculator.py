class Solution:
    def calculate(self, s: str) -> int:
        current_number =0
        stack =[]
        result = 0
        sign = 1
        for i in s:
            if i.isdigit():
                current_number = current_number *10 + int(i)
            elif i in "+-":
                result += current_number * sign
                current_number =0
                if i == "-":
                    sign = -1
                else:
                    sign =1
            elif i == "(":
                stack.append(result)
                stack.append(sign)
                result =0
                sign =1
            elif i == ")":
                result += current_number * sign
                result *= stack.pop()
                result += stack.pop()
                current_number =0
        return result + (current_number * sign)
            
        
            