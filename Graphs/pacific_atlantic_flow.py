from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # iterate over pacific and atlantic
            # bft toward equal/greater
            # if row, col in opposite bft visited add to res
    
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        pvisit = set([(0, c) for c in range(COLS)])
        for r in range(1, ROWS):
            pvisit.add((r, 0))

        avisit = set([(ROWS-1, c) for c in range(COLS)])
        for r in range(0, ROWS-1):
            avisit.add((r, COLS-1))

        def flow_from(r: int, c: int, to: int) -> None:
            if not (0 <= r < ROWS and 0 <= c < COLS and to <= heights[r][c]) or (r,c) in visit:
                return
            
            visit.add((r,c))
            q.append((r,c))

        visit = pvisit
        q = deque(list(pvisit))
        while q:
            r, c = q.popleft()
            curr = heights[r][c]
            
            flow_from(r+1, c, curr)
            flow_from(r-1, c, curr)
            flow_from(r, c+1, curr)
            flow_from(r, c-1, curr)

        visit = avisit
        q.extend(list(avisit))
        while q:
            r, c = q.popleft()
            if (r,c) in pvisit:
                res.append([r,c])

            curr = heights[r][c]
            
            flow_from(r+1, c, curr)
            flow_from(r-1, c, curr)
            flow_from(r, c+1, curr)
            flow_from(r, c-1, curr)
        
        return res