class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapk ={}
        for i, n in enumerate(nums):
            diff = target -n
            if diff in mapk:
                return [mapk[diff], i]
            mapk[n]= i
        return
                