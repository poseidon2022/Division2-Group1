class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1: return 1
        i = 0
        j = x//2
        while i<=j:
            mid = (i+j)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                j = mid - 1
            else:
                i = mid + 1
        return j