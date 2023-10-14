class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        if k==0 or k==len(nums): return nums
        i = k-1
        j = len(nums)-1
        init1,init2 = i,j
        cont = []
        while i>=0:
            cont.append(nums[i])
            nums[i] = nums[j]
            j-=1
            i-=1
        cont = cont[::-1]
        cont+=nums[init1+1:init2]
        d = init1+1
        i = 0
        print(cont)
        while d<len(nums):
            nums[d] = cont[i]
            i+=1
            d+=1
        d = 0
        while i<len(cont):
            nums[d] = cont[i]
            i+=1
            d+=1