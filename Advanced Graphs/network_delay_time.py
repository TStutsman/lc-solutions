from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # bfs weighted edges
        # heap of times:nodes
        # visited set of nodes

        adj = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj[u].append((v,t))

        heap = [(0,k)]
        visit = set()
        total = -1

        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue

            visit.add(node)
            total = time
            for nei, t in adj[node]:
                heapq.heappush(heap, (time + t, nei))
        
        return total if len(visit) == n else -1