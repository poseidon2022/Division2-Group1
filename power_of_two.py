class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def two(n):
            if n<1:
                return False
            if n==1:
                return True
            return two(n/2)
        return two(n)