class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        ans = []
        for i in points:
            distance.append((i[0]**2 + i[1]**2,i))
        
        heapq.heapify(distance)
        for i in range(k):
            ans.append(heapq.heappop(distance)[1])
        return ans