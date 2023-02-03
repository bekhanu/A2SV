class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        slack =[]
        cur_min=nums[0]
        
        for n in nums[1:]:
            while slack and n > slack[-1][0]:
                slack.pop()
                
            if slack and n < slack[-1][0] and n> slack[-1][1]:
                return True
            slack.append([n, cur_min])
            cur_min = min(cur_min , n)
        return False