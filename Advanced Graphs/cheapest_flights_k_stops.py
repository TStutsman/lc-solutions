from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adjacency list
        # dijkstra weighted path search
        # stop at k depth

        # O(f) time and space
        adj = [[] for _ in range(n)]

        for fr, to, cost in flights:
            adj[fr].append((cost, to))

        # O(f) space
        q = [(0, src, 0)]

        while q:
            # O(k * logf)
            total, cur, depth = heapq.heappop(q)

            if cur == dst:
                return total
            
            if depth > k:
                continue

            for cost, nxt in adj[cur]:
                heapq.heappush(q, (total + cost, nxt, depth + 1))
        
        return -1