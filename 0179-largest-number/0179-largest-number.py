class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        def compare(n1, n2):
            if n1+n2 > n2 + n1:
                return -1
            else:
                return 1
        nums= sorted(nums, key = cmp_to_key(compare))
        return str(int("".join(nums)))
            
#         nums = [str(x) for x in nums]
#         nums.sort(reverse= True)
#         return ''.join([str(x) for x in nums])
        
#             # num[0][0]

