class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] not in row_set:
                    if board[i][j] != ".":
                        row_set.add(board[i][j])
                    else:
                        continue
                else: 
                    return False
        
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] not in col_set:
                    if board[j][i] != ".":
                        col_set.add(board[j][i])
                    else:
                        continue
                else: 
                    return False
        grid_dict = {}
        for i in range(9):
            for j in range(9):
                grid = str(i//3) +  str(j//3)
                if board[i][j] != ".": 
                    if grid not in grid_dict.keys():
                        grid_dict[grid] = [board[i][j]]
                    else:
                        if board[i][j] not in grid_dict[grid]:
                            grid_dict[grid].append(board[i][j])
                        else:
                            return False
                else:
                    continue
        
        return True