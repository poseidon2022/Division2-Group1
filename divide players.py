class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sum,i = 0,0
        j = len(skill) - 1
        sum+=skill[i] + skill[j]
        chem = 0
        while i<j:
            if i>0 and skill[i] + skill[j]!=sum:
                return -1
            chem+=skill[i] * skill[j]
            i+=1
            j-=1
        return chem