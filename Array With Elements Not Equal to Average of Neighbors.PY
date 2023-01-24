class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
           checked = False
        while(checked != True):
            checked = True
            for i in range(1, len(nums) - 1):
                if nums[i] == (nums[i+1]+nums[i-1])//2:
                    nums[i], nums[-1] = nums[-1], nums[i]
                    checked = False
        return nums
