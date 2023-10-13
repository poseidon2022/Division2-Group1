class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        mine = defaultdict(lambda:0)
        i = 0
        j = 10
        while j<=len(s):
            print(s[i:j])
            mine[s[i:j]]+=1
            i+=1
            j+=1
        print(mine)
        for i in mine:
            if mine[i]>1: ans.append(i)
        
        return ans