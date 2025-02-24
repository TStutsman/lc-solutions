import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = [((x*x + y*y), x, y) for x,y in points]
        heapq.heapify(dist)

        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(dist)
            res.append([x, y])
        
        return res