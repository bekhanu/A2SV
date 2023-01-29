class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i, j = 0, len(piles)-1
        count = 0

        while(i<j):
            count += piles[j-1]
            j -= 2
            i += 1

        return count    
