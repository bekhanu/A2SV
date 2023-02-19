class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack = []
        stack1= []
        for i in points:
            distance = sqrt(i[0]**2 + i[1]**2)
            stack.append((distance, i))
        s = sorted(stack)
        
        for j in s:
            stack1.append(j[1])
        return stack1[0:k]