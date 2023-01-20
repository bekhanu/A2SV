class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        number = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                number.append(i)
        
        return number


