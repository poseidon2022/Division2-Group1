class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def checker(num):
            if num%4==0 and num!=0:
                num = num/4
                return checker(num)
            return num==1
        return checker(n)