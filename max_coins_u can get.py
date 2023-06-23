class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        count = 0
        p = len(piles)
        sum = 0
        for i in range(p//3):
            if count <= (p-3):
                sum+=piles[count+1]
                count+=2
            else:
                break
        return sum