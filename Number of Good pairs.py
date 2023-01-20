class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    l.append((i,j))
                else:
                    continue
        
        print(*l)
        return len(l)
        
        
                    
