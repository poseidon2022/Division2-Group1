class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productLeft = list()
        productRight = list()
        new_list = list()
        product = 1
        productLeft.append(1)
        for i in range(1,len(nums)):
            product*=nums[i-1]
            productLeft.append(product)
        nums.reverse()
        productRight.append(1)
        productt = 1
        for i in range(1,len(nums)):
            productt*=nums[i-1]
            productRight.append(productt)
        productRight.reverse()
        for i in range(len(nums)):
            new_list.append(productLeft[i]*productRight[i])
        return new_list