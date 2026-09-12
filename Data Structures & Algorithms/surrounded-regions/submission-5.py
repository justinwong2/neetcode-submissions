class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #basically i need to find all regions
        #for each region, i need to check if it is at the end of one of the boards
        #if it is not, replace all with X
        from collections import deque
        visited = {}
        def bfs(node, flip):
            nonlocal visited

            q = deque()
            q.append(node)
            while q:
                curr = q.popleft()
                x = curr[0]
                y = curr[1]
                if flip:
                    board[x][y] = "X"
                if x - 1 >= 0 and board[x-1][y] == "O" and (x-1,y) not in visited:
                    q.append((x-1, y))
                    visited[(x-1,y)] = 1
                if x + 1 < len(board) and board[x+1][y] == "O" and (x+1,y) not in visited:
                    q.append((x+1, y))
                    visited[(x+1,y)] = 1
                if y - 1 >= 0 and board[x][y-1] == "O" and (x,y-1) not in visited:
                    q.append((x, y-1))
                    visited[(x,y-1)] = 1
                if y + 1 < len(board[0]) and board[x][y+1] == "O" and (x,y+1) not in visited:
                    q.append((x, y+1))
                    visited[(x,y+1)] = 1


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited and (row == 0 or row ==len(board)-1 or col == 0 or col == len(board[0])-1):
                    visited[(row,col)] = 1
                    bfs((row,col), 0)
                    

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    bfs((row,col),1)
                    visited[(row,col)] = 1


        


        