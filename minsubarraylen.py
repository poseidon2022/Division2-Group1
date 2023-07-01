class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j,summation = 0,0,0
        length = list()
        while j < len(nums):
            summation+=nums[j]
            while summation>=target:
                length.append(j-i+1)
                summation-=nums[i]
                i+=1
            j+=1
        if len(length)==0:return 0
        return min(length)