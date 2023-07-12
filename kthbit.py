class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def build(n):
            if n==1:
                return '0'
            s = build(n-1)
            new = str()
            for i in s:
                if i=='0': new+='1'
                else: new+='0'
            return s + "1" + new[::-1]
        return build(n+1)[k-1]