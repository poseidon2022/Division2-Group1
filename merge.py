class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while i<m and nums2:
            if nums1[i]>nums2[0]:
                nums1[i],nums2[0] = nums2[0],nums1[i]
                j = 0
                while j<len(nums2)-1:
                    if nums2[j]>nums2[j+1]:
                        nums2[j],nums2[j+1] = nums2[j+1],nums2[j]
                    j+=1
            i+=1
        j = 0
        while j<len(nums2):
            nums1[i] = nums2[j]
            i+=1
            j+=1