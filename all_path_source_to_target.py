class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = list()
        def helper(graph,gra,mine):
            if mine[-1]==len(graph)-1: 
                ans.append(mine[:])
                return
            for i in gra:
                mine.append(i)
                helper(graph,graph[i],mine)
                mine.pop()

        helper(graph,graph[0],[0])
        return ans