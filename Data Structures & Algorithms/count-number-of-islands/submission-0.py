class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return count

        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

        count = 0

        def dfs(row, col):
            #set the current one to visited
            #visit the adjacent nodes 
            visited[row][col] = 1
            if row + 1 < len(grid) and grid[row+1][col] == '1' and visited[row+1][col] == 0:
                dfs(row + 1, col)
            if row -1 >= 0 and grid[row-1][col] == '1' and visited[row-1][col] == 0:
                dfs(row - 1, col)
            if col + 1 < len(grid[0]) and grid[row][col+1] == '1' and visited[row][col+1] == 0:
                dfs(row, col + 1)
            if col - 1 >= 0 and grid[row][col-1] == '1' and visited[row][col-1] == 0:
                dfs(row, col - 1)
                

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if visited[row][col]:
                    continue
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        
        return count
