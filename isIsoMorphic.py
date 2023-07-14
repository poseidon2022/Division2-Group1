class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mine = defaultdict(lambda:0)
        mine2 = defaultdict(lambda:0)
        for i in range(len(s)):
            if mine[s[i]]!=0 and t[i]!=mine[s[i]]:
                return False
            if mine2[t[i]]!=0 and s[i]!=mine2[t[i]]:
                return False
            mine2[t[i]] = s[i]
            mine[s[i]] = t[i]
        return True