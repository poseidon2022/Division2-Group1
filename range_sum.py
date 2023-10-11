class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        prefix = self.nums[:]
        for i in range(left+1,right+1):
            prefix[i] = prefix[i-1] + self.nums[i]
        return prefix[right]