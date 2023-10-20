class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        for i in range(len(matrix)):
            for j in range(1,len(matrix[i])):
                matrix[i][j] = matrix[i][j-1] + matrix[i][j]
        print(matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1,row2+1):
            if col1-1>=0:
                total+= self.matrix[i][col2]-self.matrix[i][col1-1]
            else: total+=self.matrix[i][col2]
        return total