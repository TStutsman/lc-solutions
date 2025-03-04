from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # for each node in range n
            # if not visited:
                # component count += 1
                # dfs with visit set

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        def dfs(node: int) -> None:
            for nxt in adj[node]:
                if nxt not in visit:
                    visit.add(nxt)
                    dfs(nxt)

        count = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                count += 1
                dfs(node)
            
        return count