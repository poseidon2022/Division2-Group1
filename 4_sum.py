class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        tracker = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k = j+1
                l = len(nums)-1
                while k<l:
                    temp = nums[i]+nums[j]+nums[k]+nums[l]
                    if temp==target:
                        tracker.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
                        k+=1
                        l-=1
                    elif temp>target:
                        l-=1
                    else:
                        k+=1
        ans = []
        for i in tracker: ans.append(list(i))
        return ans