class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1: return 1
        count = 0
        i,j = 0,1
        track = []
        ans = []
        while j<len(arr):
            cond = (arr[j]>arr[j-1])
            if not track and arr[j]==arr[j-1]:
                if count%2==0: count+=1
                j+=1
                continue
            if not track:
                if count==1: count+=1
                else: count+=2
                track.append(cond)
            else:
                if ((track[-1]==False and cond) or (track[-1]==True and not cond)) and (arr[j]!=arr[j-1]):
                    count+=1
                    track.append(cond)
                else:
                    ans.append(count)
                    while track: track.pop()
                    if arr[j]!=arr[j-1]:
                        count=2
                        track.append(cond)
                    else: count = 0
            j+=1
        ans.append(count)
        return max(ans)