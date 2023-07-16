class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        def backtrack(perm,visited):
            if len(perm)==len(nums):
                ans.append(perm[:])
                return

            for j in nums:
                if j in visited: continue
                perm.append(j)
                visited.add(j)
                backtrack(perm,visited)
                perm.pop()
                visited.remove(j)
        
        backtrack([],set())
        return ans