class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsidx= {n :i for i, n in enumerate(nums1)}
        stack =[]
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            cur =nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = numsidx[val]
                res[idx] = cur
            if cur in numsidx:
                stack.append(cur)
        return res