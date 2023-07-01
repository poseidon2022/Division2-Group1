class Solution:
    def arraySortedOrNot(self, arr, n):
        i = 0
        j = 1
        while j<len(arr):
            if arr[i]<=arr[j]:
                i+=1
                j+=1
                continue
            return 0
        return 1