class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = list()
        n = len(stones)
        while n>1:
            heapq._heapify_max(stones)
            temp.append(heapq._heappop_max(stones))
            if len(temp)==2:
                if temp[0]==temp[1]:
                    n-=2
                else:
                    n-=1 
                    stones.append(abs(temp[0] - temp[1]))
                temp = list()
        if stones: return stones[0]
        return 0
