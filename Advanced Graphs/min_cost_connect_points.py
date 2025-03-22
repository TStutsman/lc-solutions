from typing import List

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         # brute force - for each point, add the next closest point
#         connected = [points[0]]
#         remaining = set([tuple(point) for point in points])
#         remaining.discard(tuple(points[0]))
#         cost = 0

#         # O(n^3)
#         while len(connected) < len(points):
#             min_dist = float('inf')
#             min_point = None
#             for conn in connected:
#                 for rem in list(remaining):
#                     dist = abs(rem[0]-conn[0]) + abs(rem[1]-conn[1])
#                     if dist < min_dist:
#                         min_point = rem
#                         min_dist = dist
#             connected.append(min_point)
#             remaining.discard(min_point)
#             cost += min_dist
        
#         return cost

import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # for point, add distances to all points to heap O(nlogn)
        # pop closest unvisited point O(1)
        # for closest point, add distances to heap (compare to existing values?) O(nlogn)
        # etc. (not repeating work)
        # O(n*nlogn)

        visit = set()
        min_dist = [(0, tuple(points[0]))]
        cost = 0

        # O(n^2logn)
        while len(visit) < len(points):
            dist, curr = heapq.heappop(min_dist)
            if curr in visit:
                continue
            visit.add(curr)
            cost += dist

            for point in points:
                if tuple(point) not in visit:
                    next_dist = abs(curr[0]-point[0]) + abs(curr[1]-point[1])
                    heapq.heappush(min_dist, (next_dist, tuple(point)))
        
        return cost