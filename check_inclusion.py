class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mine = dict()
        window = dict()
        ans = list()
        for i in s1:
            mine[i] = mine.get(i,0) + 1
        i = 0 
        j = 0
        while j<len(s2):
            while j<len(s2) and j-i+1<=len(s1):
                window[s2[j]] = window.get(s2[j],0) + 1
                j+=1
            if window==mine:
                return True
            if window.get(s2[i],0)>1:
                window[s2[i]]-=1
            else:
                window.pop(s2[i])
            i+=1
        return False

