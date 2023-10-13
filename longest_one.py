class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        count,chan = 0,0
        ans = []
        while j<len(nums):
            if nums[j]==1: count+=1
            elif nums[j]!=1:
                if chan<1:
                    chan+=1
                else:
                    ans.append(count)
                    while True:
                        if nums[i]==1: count-=1
                        else:
                            i+=1
                            break
                        i+=1
            j+=1
        if chan==0: ans.append(count-1)
        else: ans.append(count)
        return max(ans)