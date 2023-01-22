class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
       
        d = abs(dividend)
        dv = abs(divisor)
        num = 0
        
        while d>= dv:
            tmp = dv
            mul = 1
            while d>=tmp:
                d-=tmp
                num +=mul
                mul+=mul
                tmp +=tmp
            
        if (dividend <0 and divisor >=0) or (divisor <0 and dividend >=0):
            
            num = -num
        # else:
        #     num =round(dividend / divisor)
            
        return min(2147483647, max(-2147483648, num))