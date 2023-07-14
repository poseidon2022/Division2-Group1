class Solution:
    def firstUniqChar(self, s: str) -> int:
        mine = defaultdict(lambda:0)
        for i in s:
            mine[i]+=1
            if mine[i]>1:
                mine[i] = float('-inf')
        for i in mine:
            if mine[i]!=float('-inf'):
                return s.index(i)
        return -1