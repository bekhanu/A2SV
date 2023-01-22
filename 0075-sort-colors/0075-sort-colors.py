class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] == 0:
                print("red")
            elif nums[i] ==1:
                print("white")
            else:
                if nums[i] ==2:
                    print("blue")
        """
        Do not return anything, modify nums in-place instead.
        """
        