class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        neg = num
        num = abs(num)
        if num ==0:
            return "0"
        while num > 0:
            remainder= num % 7
            result += str(remainder)
            num //= 7
        if neg <0:
            return ("-"+result[::-1])
        else:
            return (result[::-1])