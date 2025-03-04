from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree requirements:
            # No cycles
            # All nodes are in the tree

        # adj map and dfs with visit set
        adj = [[] for _ in range(n)]
        visit = set()
        for v, x in edges:
            adj[v].append(x)
            adj[x].append(v)
        
        def dfs(prev: int, node: int) -> bool:
            if node in visit:
                return False
            visit.add(node)

            for nxt in adj[node]:
                if nxt != prev and not dfs(node, nxt):
                    return False
            
            return True

        if dfs(None, 0):
            return len(visit) == n
        return False