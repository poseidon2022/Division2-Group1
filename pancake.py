class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        _max = len(arr)
        for i in range(len(arr)-1,-1,-1):
            idx = arr[:i+1].index(_max)
            if idx==i:
                _max-=1
                continue
            if idx!=0: arr = arr[:idx+1][::-1] + arr[idx+1:]
            arr[:i+1] = arr[:i+1][::-1]
            if idx!=0: ans.append(idx+1)
            ans.append(i+1)
            _max-=1
        return ans