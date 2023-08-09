class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        ans.append([])
        def helper(nums,mine,o):
            for i in range(o,len(nums)):
                mine.append(nums[i])
                if sorted(mine) not in ans: ans.append(sorted(mine[:]))
                helper(nums,mine,i+1)
                mine.pop()
            return 
        helper(nums,[],0)
        return ans