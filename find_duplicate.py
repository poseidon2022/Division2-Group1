class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        mine = defaultdict(list)
        for i in paths:
            lst = i.split()
            for j in lst[1:]:
                content = j[j.index('(')+1:j.index(')')]
                mine[content].append((lst[0],j[:j.index('(')]))
        
        for i in mine:
            if len(mine[i])>1:
                cont = []
                for j in mine[i]:
                    cont.append(j[0]+'/'+j[1])
                ans.append(cont)
        return ans