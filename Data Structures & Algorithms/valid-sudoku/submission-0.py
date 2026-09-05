class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows = {(1,0), (2,0)...{9,0}}
        #columns = {(0,1), (0,2)... (0,9)}
        dict_row = {}
        dict_col = {}
        dict_box = {}

        for row in range(len(board)):
            dict_row[(row, 0)] = set()
            for col in range(len(board[row])):
                if row == 0:
                    dict_col[(row, col)] = set()
                if row % 3 == 0 and col % 3 == 0:
                    dict_box[row // 3, col // 3] = set()
                value = board[row][col]

                if value != ".":
                    if value in dict_row[(row,0)] or value in dict_col[(0,col)] or value in dict_box[(row//3, col//3)]:
                        return False
                    else:
                        dict_row[(row,0)].add(value)
                        dict_col[(0,col)].add(value)
                        dict_box[(row//3, col//3)].add(value)
        return True     
