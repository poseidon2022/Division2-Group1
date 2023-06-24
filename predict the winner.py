class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def recursion(start,end):
            if start>end:
                return 0
            starting,ending = nums[start],nums[end]
            left = recursion(start+1,end)
            right = recursion(start,end-1)
            return max(starting - left,ending - right)
        return recursion(0,len(nums)-1)>=0