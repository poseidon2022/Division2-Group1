class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(number,exponent):
            if exponent<0:
                return power(1/number,-exponent+1) * number
            if exponent==1:
                return number
            return power(number,exponent-1) * number
        return power(x,n)