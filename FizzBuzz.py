class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        get=list()
        for i in range(1 , n+1):
            if i % 3 == 0 and i % 5 == 0:
                get.append("FizzBuzz")
            elif i % 3 ==0:
                get.append("Fizz")
            elif i % 5 == 0:
                get.append("Buzz")
            else:
                get.append(str(i))    
        return get 
