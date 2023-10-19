class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        pref = [0]*len(nums)
        if zeros>1: return pref
        prod = 1
        for i in range(len(nums)):
            if nums[i]!=0: prod*=nums[i]
        if zeros==0: return [prod//_ for _ in nums]
        else: return [0 if i!=0 else prod for i in nums]