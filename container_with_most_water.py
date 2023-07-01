class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        init_area = 0
        while i<j:
            one = height[i]
            two = height[j]
            if min(one,two)*(j-i) > init_area:
                init_area = min(one,two)*(j-i)
            if min(one,two) == one:
                i+=1
            elif min(one,two)==two:
                j-=1
        return init_area