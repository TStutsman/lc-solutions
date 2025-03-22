from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # bfs with heap
        # visited = [False * x] * y
        # res = 0
        # while heap starting with 0,0
            # res = max(res, curr_height)
            # if curr is right corner 
                # return res

            # add unvisited neighbors
        ROWS, COLS = len(grid), len(grid[0])
        NSEW = [(0,1),(0,-1),(1,0),(-1,0)]

        heap = [(grid[0][0],0,0)]
        # O(n^2) space
        visit = [[False] * COLS for _ in grid]
        visit[0][0] = True
        res = 0

        # O(n^2logn)
        while heap:
            height, r, c = heapq.heappop(heap)
            res = max(res, height)

            if (r,c) == (ROWS-1,COLS-1):
                return res

            for ns, ew in NSEW:
                nr, nc = r+ns, c+ew
                if 0 <= nc < COLS and 0 <= nr < ROWS and not visit[nr][nc]:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
                    visit[nr][nc] = True