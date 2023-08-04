class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mine = list()
        another = list()
        for i in range(len(mat)):
            while mat[i]:
                heapq.heapify(mat[i])
                if mat[i][0]==1: break
                heapq.heappop(mat[i])

            mine.append((len(mat[i]),i))
        mine.sort()
        for j in range(k):
            another.append(mine[j][1])
        return another