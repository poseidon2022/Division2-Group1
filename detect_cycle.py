class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ans = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(row, col, prev_row, prev_col):
            visited.add((row,col))
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and ((new_row,new_col)!=(prev_row,prev_col)) and grid[new_row][new_col]==grid[row][col]:         
                    if (new_row,new_col) in visited:
                        return True
                    elif dfs(new_row,new_col,row,col):
                        return True
            return False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and dfs(i,j,None,None):
                    return True
        return False
