class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        my_arr = list()
        while i<j:
            if numbers[i] + numbers[j] < target:
                i+=1
                continue
            elif numbers[i] + numbers[j] > target:
                j-=1
                continue
            my_arr.append(i+1)
            my_arr.append(j+1)
            break
        return my_arr