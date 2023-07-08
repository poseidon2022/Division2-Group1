class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        my_stack = list()
        temp = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<temp:
                return True    
            while my_stack and my_stack[-1]<nums[i]:
                temp = my_stack.pop()
            my_stack.append(nums[i])
        return False