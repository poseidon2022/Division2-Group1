class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    graph[i].append(j)

        visited = set()
        def helper(node,visited):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    helper(i,visited)
            return 1
        
        count  = 0
        for i in graph:
            if i not in visited:
                count+=helper(i,visited)
        return count