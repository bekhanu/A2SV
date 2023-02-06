class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        i =0
        x = 1
        while x <=n:
            if x==n:
                return True
            i+=1
            x= 2**i
        return False