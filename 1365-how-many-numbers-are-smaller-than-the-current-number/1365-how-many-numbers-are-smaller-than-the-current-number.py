class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = [0]*101
        for i in nums:
            num[i] += 1
        cot = 0
        for j in range(len(num)):
            prev = num[j]
            num[j]= cot
            cot +=prev
        return [num[i] for i in nums]