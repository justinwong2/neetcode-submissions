class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return maximum
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

        def visit(row, col):
            if grid[row][col] == 0 or visited[row][col] == 1:
                return 0
            row1,row2,col1,col2 = 0,0,0,0
            visited[row][col] = 1
            if row - 1 >= 0 and grid[row - 1][col] == 1 and visited[row - 1][col] == 0:
                row1 = visit(row - 1, col)
            if row + 1 < len(grid) and grid[row + 1][col] == 1 and visited[row + 1][col] == 0:
                row2 = visit(row + 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == 1 and visited[row][col - 1] == 0:
                col1 = visit(row, col - 1)
            if col + 1 < len(grid[0]) and grid[row][col+1] == 1 and visited[row][col + 1] == 0:
                col2 = visit(row, col + 1)
            return 1 + row1 + row2 + col1 + col2

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == 1 or grid[row][col] == 0:
                    continue
                count = visit(row, col)
                maximum = max(maximum, count)
        
        return maximum

