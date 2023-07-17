class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        i = 0
        j = num//2
        while i<=j:
            mid = (i+j)//2
            if mid*mid==num: return True
            elif mid*mid<num: i = mid + 1
            else: j = mid - 1
        return False