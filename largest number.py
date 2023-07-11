class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            if x+y<y+x:
                return 1
            if x+y>y+x:
                return -1
            else: return 0
        from functools import cmp_to_key
        otra = list()
        if len(nums)==1:
            return str(nums[0])
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort(key = cmp_to_key(compare))
        ans  = "".join(nums)
        i = 0
        while i<len(ans):
            if ans[i]!="0": break
            ans = ans[1:]
        if ans=='':
            return '0'
        return ans