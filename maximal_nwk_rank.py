class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        _max = 0
        mine = defaultdict(list)
        for a,b in roads:
            mine[a].append(b)
            mine[b].append(a)
        for i in range(n):
            for j in range(i+1,n):
                tot = len(mine[i]) + len(mine[j])
                if tot >_max:
                    _max = tot
                    if i in mine[j]: _max-=1
        return _max
