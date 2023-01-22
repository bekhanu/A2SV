class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
#         for i in range(0, len(nums)):
#             for j in range(0, len(nums)):
#                 if nums[i]==nums[j+1]:
#                     count ==0
#                 else:
#                     if nums[i] + nums[j+1]==k:
                        
#                         count+=1
#                     break
        nums.sort()
        l, r=0, len(nums)-1
        count = 0
        while l < r:
            sums = nums[l] + nums[r]
            if sums == k:
                count += 1
                l += 1
                r -= 1
            elif sums < k:
                l += 1
            else:
                r -= 1

        return count