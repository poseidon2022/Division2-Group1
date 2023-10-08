class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(row):
            if row==0:
                return [1]
            if row==1:
                return [1,1]
            my_arr = list()
            i = 0
            d = pascal(row-1)
            while i<row-1:
                my_arr.append(d[i] + d[i+1])
                i+=1
            return [1] + my_arr + [1]
        return pascal(rowIndex)