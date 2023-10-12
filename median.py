class MedianFinder:

    def __init__(self):
        self.nums = list()
    def addNum(self, num: int) -> None:
        self.nums.append(num)
    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)//2
        if self.nums and len(self.nums)%2!=0: return float(self.nums[len(self.nums)//2])
        elif self.nums and len(self.nums)%2==0:
            return float(self.nums[n-1] + (self.nums[n]))/2