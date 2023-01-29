class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = i = 0
        count  = total = 0

        for i in range(len(nums)):
            total += nums[i]
            
            while nums[i] * (i - j + 1) > total + k:
                total -= nums[j]
                j += 1

            count = max(count, i - j + 1)

        return count
       
        
        
        