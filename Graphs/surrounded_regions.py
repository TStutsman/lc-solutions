from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # O(n + m) n = cols, m = rows
        # iterate over edges
            # bft from 'o' on the edges (not surrounded)
                # change to '.'

        ROWS, COLS = len(board), len(board[0])
        q = deque()

        # add all edges to queue
        q.extend([(0,c) for c in range(COLS)])
        q.extend([(ROWS-1,c) for c in range(COLS)])
        for r in range(1,ROWS-1):
            q.append((r,0))
            q.append((r,COLS-1))

        # BFT from edge 'O's and change to '.'
        while q:
            r, c = q.popleft()
            
            if not (0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O'):
                continue
            
            board[r][c] = '.'
            
            q.extend([(r+1,c),(r-1,c),(r,c+1),(r,c-1)])

        # O(n * m)
        # iterate over board
            # if '.' change to 'O' else 'X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'