class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for k in grid:
            i = 0
            j = len(k)-1
            while i<=j:
                mid = (i+j)//2
                if k[mid]>=0: i = mid + 1
                elif k[mid]<0: j = mid - 1

            count+=len(k)-i
        return count