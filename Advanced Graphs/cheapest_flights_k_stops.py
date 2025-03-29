from typing import List
# import heapq

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         # adjacency list
#         # dijkstra weighted path search
#         # stop at k depth

#         # O(f) time and space
#         adj = [[] for _ in range(n)]

#         for fr, to, cost in flights:
#             adj[fr].append((cost, to))

#         # O(f) space
#         q = [(0, src, 0)]

#         while q:
#             # O(k * logf)
#             total, cur, depth = heapq.heappop(q)

#             if cur == dst:
#                 return total
            
#             if depth > k:
#                 continue

#             for cost, nxt in adj[cur]:
#                 heapq.heappush(q, (total + cost, nxt, depth + 1))
        
#         return -1

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dfs k stops O(k * f)
        # track min cost to dst
        # return min or -1

        adj = [[] for _ in range(n)]
        
        for fr, to, cst in flights:
            adj[fr].append((to,cst))

        res = 1000000

        def dfs(node: int, total: int, depth: int) -> None:
            nonlocal res
            if node == dst:
                res = min(res, total)

            if depth > k:
                return
            
            for to, cost in adj[node]:
                dfs(to, total+cost, depth+1)
        
        dfs(src, 0, 0)
        return res if res < 1000000 else -1