class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0]*n
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1] + nums[i]
        mine = defaultdict(lambda:0)
        mine[0]=1
        result = 0
        print(pref)
        for i in pref:
            if i-k in mine: result+=mine[i-k]
            mine[i]+=1
        return result