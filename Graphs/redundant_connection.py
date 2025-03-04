from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find cycle and collect edges of cycle
        # choose edge of cycle that appears last in edges

        # adjacency list creation
        adj = {i:[] for i in range(1, len(edges) + 1)}
        for e, f in edges:
            adj[e].append(f)
            adj[f].append(e)

        visit, loop = set(), set()

        # dfs from node 1 with visit set
        def dfs(prev: int, node: int) -> bool:
            if node in visit:
                # cycle detected
                # need to know all nodes added after visited node
                return True
            visit.add(node)

            # iterate over adj list except previous
            for nxt in adj[node]:
                if nxt == prev:
                    continue

                if dfs(node, nxt):
                    # stop adding to loop when we reach first node added
                    if nxt in loop:
                        return False
                    # add neighbor to loop
                    loop.add(nxt)
                    return True
            return False
                    
        dfs(0, 1)
        # reverse iterate over edges:
        for e, f in edges[::-1]:
            # first edge containing two nodes in loop return
            if e in loop and f in loop:
                return [e,f]
