class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for col in range(len(board[0]))] for row in range(len(board))]

        def explore(row, col, index):
            nonlocal visited
            print(board[row][col])
            if index >= len(word):
                return True
            if row-1 >= 0 and board[row-1][col] == word[index] and visited[row-1][col] == 0:
                visited[row-1][col] = 1
                boolean = explore(row-1, col, index+1)
                visited[row-1][col] = 0
                if boolean:
                    return True
            if row+1 < len(board) and board[row+1][col] == word[index] and visited[row+1][col] == 0:
                visited[row+1][col] = 1
                boolean = explore(row+1, col, index+1)
                visited[row+1][col] = 0
                if boolean:
                    return True
            if col-1 >= 0 and board[row][col-1] == word[index] and visited[row][col-1] == 0:
                visited[row][col-1] = 1
                boolean = explore(row, col-1, index+1)
                visited[row][col-1] = 0
                if boolean:
                    return True
            if col+1 < len(board[0]) and board[row][col+1] == word[index] and visited[row][col+1] == 0:
                visited[row][col+1] = 1
                boolean = explore(row, col+1, index+1)
                visited[row][col+1] = 0
                if boolean:
                    return True
            #to catch the case where everything above doesnt run due to no matches
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                currChar = board[row][col]
                if currChar == word[0]:
                    visited[row][col] = 1
                    boolean = explore(row, col, 1)
                    visited[row][col] = 0
                    if boolean:
                        return True
        
        return False
        
        
            
        