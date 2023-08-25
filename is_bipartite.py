class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        mine = defaultdict(lambda:-1)
        queue = deque([0])
        mine[0]=1
        visited = set()
        
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            for i in graph[cur]:
                if mine[i]==-1:
                    mine[i]=int(not mine[cur])
                if mine[i]==mine[cur]:
                    return False
                if i not in visited: queue.append(i)
            if not queue and cur+1<len(graph): queue.append(cur+1)
        return True