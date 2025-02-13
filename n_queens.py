class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        row = "".join(['o' for _ in range(n)])
        board = [row for _ in range(n)]

        def place_queen(r: int, c: int):
            for row in range(n):
                if row == r:
                    for col in range(n):
                        board[row][col] = '.'
                    board[r][c] = 'Q'
                    continue
                
                for col in range(n):
                    if col == c:
                        board[row][col] = '.'
                    elif row - r == col - c or row - r == c - col:
                        board[row][col] = '.'
        
        def dfs():
            pass

        return res
