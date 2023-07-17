class Solution:
    def guessNumber(self, n: int) -> int:
        i = 0
        j = n
        while i<=j:
            mid = (i+j)//2
            res = guess(mid)
            if res==0: return mid
            elif res==1: i = mid + 1
            else: j =  mid - 1
        return mid