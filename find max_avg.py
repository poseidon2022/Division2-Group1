class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum,i,j = 0,0,0
        maxim = float('-inf')
        while j<len(nums):
            while j-i+1<=k:
                _sum+=nums[j]
                j+=1
            j-=1
            if _sum/k>maxim:
                maxim = _sum/k
            _sum-=nums[i]
            i+=1
            j+=1
        return maxim