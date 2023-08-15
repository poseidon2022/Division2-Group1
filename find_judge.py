class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        if not trust and n!=1: return -1
        for j in trust:
            graph1[j[1]].append(j[0])
            graph2[j[0]].append(j[1])
        
        for i in range(1,n+1):
            if len(graph1[i])==n-1 and graph2[i]==[]: return i

        return -1
