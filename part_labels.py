class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        mine = defaultdict(list)
        for i in range(len(s)):
            mine[s[i]].append(i)
        tobe = mine[s[0]][-1] + 1
        for i in range(1,len(s)):
            if i==tobe:
                d = sum(ans[:len(ans)])
                if not ans: ans.append(tobe)
                else: ans.append(tobe - d)
                tobe = mine[s[i]][-1]+1
            if mine[s[i]][-1]+1>tobe: tobe = mine[s[i]][-1]+1
        ans.append(tobe - sum(ans[:len(ans)]))
        return ans