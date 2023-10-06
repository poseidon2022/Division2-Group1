class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        _max = float('-inf')
        for i in piles:
            if i>_max: _max = i
        count = [0]*(_max+1)
        for i in piles: count[i]+=1
        ans = []
        for i in range(len(count)-1,-1,-1): ans+=[i]*count[i]
        _sum = 0
        tot = len(piles)//3
        i = 1
        while i<len(piles)-tot:
            _sum+=ans[i]
            i+=2
        return _sum