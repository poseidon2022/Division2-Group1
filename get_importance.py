class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mine = defaultdict()
        for i in range(len(employees)):
            mine[employees[i].id]=(employees[i].importance,employees[i].subordinates)
        
        ans = []
        def helper(id,mine):
            importance = mine[id][0]
            ans.append(importance)
            if not mine[id][1]:
                return
            
            for i in mine[id][1]:
                helper(i,mine)
                #ans.append(importance)


        helper(id,mine)
        return sum(ans)