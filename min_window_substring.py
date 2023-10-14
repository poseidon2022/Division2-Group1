class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        mine = defaultdict(lambda:0)
        compare = set(t)
        for i in t:
            mine[i]+=1
        i, j = 0,0
        ans = ""
        final = float('inf')
        while j<len(s):
            if s[j] in compare:
                if mine[s[j]]>0: n-=1
                mine[s[j]]-=1
            if n==0:
                while n==0:
                    if s[i] in compare:
                        mine[s[i]]+=1
                        if mine[s[i]]>0: n+=1
                    i+=1
                if len(s[i-1:j+1])<final:
                    ans = s[i-1:j+1]
                    final = len(ans)


            j+=1
        
        return ans