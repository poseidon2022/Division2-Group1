class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = list()
        heapq.heapify(minHeap)
        for i in range(len(heights)-1):
            dif = heights[i+1] - heights[i]
            if dif>0: heapq.heappush(minHeap,dif)
            if len(minHeap)>ladders: bricks-=heapq.heappop(minHeap)
            if bricks<0: return i 

        return len(heights) - 1