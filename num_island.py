lass Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(grid, visited, row, col):
            if grid[row][col]=="0":
                return False

            visited[row][col] = True

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)
            
            return True
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j]!="0":
                    count+=dfs(grid,visited,i,j)
        
        return count