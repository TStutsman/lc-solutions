# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         row = "".join(['o' for _ in range(n)])
#         board = [row for _ in range(n)]

#         def place_queen(r: int, c: int):
#             for row in range(n):
#                 if row == r:
#                     for col in range(n):
#                         board[row][col] = '.'
#                     board[r][c] = 'Q'
#                     continue
                
#                 for col in range(n):
#                     if col == c:
#                         board[row][col] = '.'
#                     elif row - r == col - c or row - r == c - col:
#                         board[row][col] = '.'
        
#         def dfs():
#             pass

#         return res

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        # due to the dfs implementation, no need to check row
        def safe_queen(r: int, c: int) -> bool:
            # check if the column is clear
            for row in range(n):
                if board[row][c] == 'Q':
                    return False
            
            # check diagonals (queens are only in rows lower than r)
            for i in range(1, r + 1):
                if c + i < n and board[r-i][c+i] == 'Q':
                    return False
                elif c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                        
            return True
        
        def dfs(row: int) -> None:
            if row >= n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if safe_queen(row, col):
                    board[row][col] = 'Q'
                    dfs(row + 1)
                    board[row][col] = '.'
        
        dfs(0)

        return res
