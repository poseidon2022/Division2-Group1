class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while i<=j:
            mid = (i+j)//2
            res = isBadVersion(mid)
            if res==False: i = mid + 1
            elif res==True: j = mid - 1
        return i