class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = defaultdict(lambda:-1)
        my_stack = list()
        ans = list()
        for i in nums2:
            if not my_stack or my_stack[-1]>i:
                my_stack.append(i)
                continue
            while my_stack and my_stack[-1]<i:
                my_dict[my_stack[-1]] = i
                my_stack.pop()
            my_stack.append(i)
        for i in nums1:
            ans.append(my_dict[i])
        return ans