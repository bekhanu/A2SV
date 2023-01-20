import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # def find_kth_largest(nums, k):
        #     return heapq.nlargest(k, nums)[-1]
        # k = nums[0]
        # for i in nums:
        #     if k >i:
        #         k 
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort(reverse=True)
        return str(nums[k-1])

#         sorted_nums = sorted(nums,reverse = True)
#         kth_larg = sorted_nums[k-1]
               
                
            
#         return kth_larg
    
    
#     return arr[k-1] 
  

# print(kthLargestNumber(arr, k)) 
