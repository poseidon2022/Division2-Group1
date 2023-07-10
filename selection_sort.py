class Solution: 
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            temp = i
            for j in range(i+1,len(arr)):
                if arr[temp]>arr[j]:
                    temp = j
            arr[i],arr[temp] = arr[temp],arr[i]
                
                
        return arr
