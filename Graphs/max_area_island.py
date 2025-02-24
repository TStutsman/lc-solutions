class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            e = dfs(r+1, c)
            w = dfs(r-1, c)
            s = dfs(r, c+1)
            n = dfs(r, c-1)

            return 1 + n + e + s + w

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))

        return max_area