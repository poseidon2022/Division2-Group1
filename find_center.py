class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mine = defaultdict(list)
        for i in edges:
            mine[i[0]].append(i[1])
            if len(mine[i[0]])==len(edges):
                return i[0]
            mine[i[1]].append(i[0])
            if len(mine[i[1]])==len(edges):
                return i[1]