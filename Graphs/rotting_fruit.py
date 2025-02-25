from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # iterating over grid
            # fresh counter
            # multi-origin bft from rotting fruits

        # if fresh remaining -> -1
        # else return minutes

        ROWS, COLS = len(grid), len(grid[0])
        fresh, minutes = 0, 0
        q = deque()
        visit = set()

        def addFruit(r: int, c: int) -> None:
            if not (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1) or (r,c) in visit:
                return
            
            visit.add((r,c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    addFruit(r+1, c)
                    addFruit(r-1, c)
                    addFruit(r, c+1)
                    addFruit(r, c-1)
        
        time = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                fresh -= 1
                minutes = max(minutes, time)

                addFruit(r+1, c)
                addFruit(r-1, c)
                addFruit(r, c+1)
                addFruit(r, c-1)

            time += 1

        return minutes if not fresh else -1