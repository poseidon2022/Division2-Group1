class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mine = defaultdict(list)
        ans = []
        visited = set()
        for i in edges:
            mine[i[0]].append(i[1])
            mine[i[1]].append(i[0])
        if n==1 and not edges: return True
        def helper(source,destin,mine,visited):
            if mine[source]==[]:
                return
            if destin in mine[source]:
                ans.append(True)
                return
            for i in range(len(mine[source])):
                if mine[source][i] in visited: continue
                visited.add(source)
                helper(mine[source][i],destin,mine,visited)





        helper(source,destination,mine,visited)
        return True in ans