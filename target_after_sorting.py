class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        _max = float('-inf')
        for i in nums:
            if i>_max: _max = i
        count = [0]*(_max+1)
        for i in nums:
            count[i]+=1
        mine = []
        for i in range(len(count)):
            mine+=[i]*count[i]
        ans = []
        for i in range(len(mine)):
            if mine[i]==target: ans.append(i)
        return ans