class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mine = dict()
        window = dict()
        ans = list()
        for i in p:
            mine[i] = mine.get(i,0) + 1
        i = 0 
        j = 0
        while j<len(s):
            while j<len(s) and j-i+1<=len(p):
                window[s[j]] = window.get(s[j],0) + 1
                j+=1
            if window==mine:
                ans.append(i)
            if window.get(s[i],0)>1:
                window[s[i]]-=1
            else:
                window.pop(s[i])
            i+=1
        return ans