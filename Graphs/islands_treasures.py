from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        # bf traverse from t-chests

        # iterate over array
            # not t-chest:
                # skip / continue

            # found t-chest -> begin BFT
            # new visited set
            # BFT queue ( row | column | depth ) vals
                # if visited or depth > grid val:
                    # skip / continue
                # else modify grid, add visited, add neighbors
        
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    continue
                
                visited = set([(r,c)])
                queue = deque([(r+1, c, 1),(r-1, c, 1),(r, c+1, 1),(r, c-1, 1)])

                while queue:
                    cr, cc, cd = queue.popleft()
                    if cr < 0 or cc < 0 or cr >= ROWS or cc >= COLS or (cr, cc) in visited or cd > grid[cr][cc]:
                        continue

                    grid[cr][cc] = cd
                    visited.add((cr,cc))
                    queue.extend([(cr+1, cc, cd+1),(cr-1, cc, cd+1),(cr, cc+1, cd+1),(cr, cc-1, cd+1)])