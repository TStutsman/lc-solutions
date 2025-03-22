from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # brute force - for each point, add the next closest point
        connected = [points[0]]
        remaining = set([tuple(point) for point in points])
        remaining.discard(tuple(points[0]))
        cost = 0

        # O(n^3)
        while len(connected) < len(points):
            min_dist = float('inf')
            min_point = None
            for conn in connected:
                for rem in list(remaining):
                    dist = abs(rem[0]-conn[0]) + abs(rem[1]-conn[1])
                    if dist < min_dist:
                        min_point = rem
                        min_dist = dist
            connected.append(min_point)
            remaining.discard(min_point)
            cost += min_dist
        
        return cost