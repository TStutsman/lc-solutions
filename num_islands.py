from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> None:
            queue = deque([(r,c)])

            while(queue):
                r,c = queue.popleft()

                if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                    continue

                if grid[r][c] == "1":
                    grid[r][c] = "*"

                    queue.extend([(r+1, c), (r-1,c), (r, c+1), (r, c-1)])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
            
        return count