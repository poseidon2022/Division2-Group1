class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        ans = list()
        def backtrack(i,comb):
            if len(comb)==k:
                ans.append(comb[:])
                return 
            if i>=n: return

            comb.append(nums[i])
            backtrack(i+1,comb)
            comb.pop()
            backtrack(i+1,comb)

        backtrack(0,[])
        return ans